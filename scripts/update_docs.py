"""
This script runs Apache Airflow in a Docker container, connects
to its PostgreSQL database, and creates mermaid diagrams from the reflected
database schema.
"""

from __future__ import annotations

import os
from functools import cache
from pathlib import Path
from shutil import which
from subprocess import check_call
from tempfile import NamedTemporaryFile
from typing import Any
from urllib.request import urlopen

from sqlalchemy import Connection, create_engine
from yaml import safe_load

AIRFLOW_DOCKER_COMPOSE_URL: str = (
    "https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml"
)


@cache
def download_docker_compose_yaml() -> Path:
    """
    Get the Docker Compose file for Apache Airflow.
    """
    temp_file_path: Path
    with (
        urlopen(AIRFLOW_DOCKER_COMPOSE_URL) as response,  # noqa: S310
        NamedTemporaryFile("wb", delete=False) as binary_file,
    ):
        binary_file.write(response.read())
        temp_file_path = Path(binary_file.name)
    return temp_file_path


def get_postgresql_url(docker_compose_yaml: Path | None = None) -> str:
    docker_compose_yaml = docker_compose_yaml or download_docker_compose_yaml()
    with open(docker_compose_yaml) as text_file:
        docker_compose: dict[str, dict[str, Any]] = safe_load(text_file)
    return docker_compose["x-airflow-common"]["environment"][
        "AIRFLOW__DATABASE__SQL_ALCHEMY_CONN"
    ].replace("psycopg2", "psycopg")


def write_env(directory: Path) -> None:
    with open(directory / ".env", "w") as env_file:
        env_file.write(f"AIRFLOW_UID={os.getuid()}\n")


def main() -> None:
    docker_compose_yaml: Path = download_docker_compose_yaml()
    postgresql_url: str = get_postgresql_url(docker_compose_yaml)
    write_env(docker_compose_yaml.parent)
    check_call(
        [
            which("docker") or "docker",
            "compose",
            "--file",
            str(docker_compose_yaml),
            "--project-directory",
            str(docker_compose_yaml.parent),
            "up",
            "-d",
        ],
    )
    try:
        print("!!!", str(postgresql_url))
        connection: Connection
        with create_engine(postgresql_url).connect() as connection:
            for row in connection.execute(
                "select * from information_schema.tables"
            ).fetchall():
                print(row)
    finally:
        check_call(
            [
                which("docker") or "docker",
                "compose",
                "--file",
                str(docker_compose_yaml),
                "--project-directory",
                str(docker_compose_yaml.parent),
                "down",
            ],
        )
        print("Airflow PostgreSQL container stopped.")


if __name__ == "__main__":
    main()
