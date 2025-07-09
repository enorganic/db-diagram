from __future__ import annotations

from urllib.request import urlopen

AIRFLOW_DOCKER_COMPOSE_URL: str = (
    "https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml"
)


def main() -> None:
    # AIRFLOW__DATABASE__SQL_ALCHEMY_CONN
    with (
        urlopen(AIRFLOW_DOCKER_COMPOSE_URL) as response,  # noqa: S310
        open("airflow-docker-compose.yaml", "wb"),
    ):
        print(response.read().decode())


if __name__ == "__main__":
    main()
