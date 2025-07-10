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

from yaml import dump, safe_load

from db_diagram._mermaid import write_markdown, write_mermaid_images

AIRFLOW_DOCKER_COMPOSE_URL: str = (
    "https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml"
)
DOCS_EXAMPLES_DIRECTORY: Path = (
    Path(__file__).absolute().parent.parent / "docs" / "examples"
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
    with open(temp_file_path) as text_file:
        docker_compose: dict[str, dict[str, Any]] = safe_load(text_file)
    docker_compose["services"]["postgres"]["ports"] = ["5432:5432"]
    with open(temp_file_path, "w") as text_file:
        dump(docker_compose, text_file)
    return temp_file_path


def get_postgresql_url(docker_compose_yaml: Path | None = None) -> str:
    docker_compose_yaml = docker_compose_yaml or download_docker_compose_yaml()
    with open(docker_compose_yaml) as text_file:
        docker_compose: dict[str, dict[str, Any]] = safe_load(text_file)
    return (
        docker_compose["x-airflow-common"]["environment"][
            "AIRFLOW__DATABASE__SQL_ALCHEMY_CONN"
        ]
        .replace("psycopg2", "psycopg")
        .replace("@postgres/", "@127.0.0.1:5432/")
    )


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
        for depth in range(1, 4):
            write_markdown(
                postgresql_url,
                DOCS_EXAMPLES_DIRECTORY
                / "airflow"
                / f"depth={depth}"
                / "diagrams.md",
                depth=depth,
                title="Airflow PostgreSQL Database Diagrams",
            )
            write_markdown(
                postgresql_url,
                DOCS_EXAMPLES_DIRECTORY
                / "airflow"
                / f"depth={depth}"
                / "ab-diagrams.md",
                depth=depth,
                title="Airflow ab_* PostgreSQL Database Diagrams",
                include=("ab_*",),
            )
            write_markdown(
                postgresql_url,
                DOCS_EXAMPLES_DIRECTORY
                / "airflow"
                / f"depth={depth}"
                / "dag-diagrams.md",
                depth=depth,
                title="Airflow dag_* PostgreSQL Database Diagrams",
                include=("dag_*", "dag"),
            )
            write_markdown(
                postgresql_url,
                DOCS_EXAMPLES_DIRECTORY
                / "airflow"
                / f"depth={depth}"
                / "asset-diagrams.md",
                depth=depth,
                title="Airflow asset_* PostgreSQL Database Diagrams",
                include=("asset_*",),
            )
            write_markdown(
                postgresql_url,
                DOCS_EXAMPLES_DIRECTORY
                / "airflow"
                / f"depth={depth}"
                / "task-diagrams.md",
                depth=depth,
                title="Airflow task_* PostgreSQL Database Diagrams",
                include=("task_*",),
            )
            write_markdown(
                postgresql_url,
                DOCS_EXAMPLES_DIRECTORY
                / "airflow"
                / f"depth={depth}"
                / "other-diagrams.md",
                depth=depth,
                title="Airflow (other) PostgreSQL Database Diagrams",
                exclude=(
                    "ab_*",
                    "dag_*",
                    "dag",
                    "asset_*",
                    "task_*",
                ),
            )
            image_directory: Path = (
                DOCS_EXAMPLES_DIRECTORY / "airflow" / f"depth={depth}" / "svg"
            )
            write_mermaid_images(
                postgresql_url,
                directory=image_directory,
                image_format="svg",
                depth=depth,
                theme="dark",
            )
            write_markdown(
                postgresql_url,
                DOCS_EXAMPLES_DIRECTORY
                / "airflow"
                / f"depth={depth}"
                / "diagrams-svg.md",
                image_directory=image_directory,
                image_format="svg",
                depth=depth,
                title="Airflow PostgreSQL Database Diagrams",
            )
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


if __name__ == "__main__":
    main()
