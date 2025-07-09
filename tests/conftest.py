from __future__ import annotations

from shutil import rmtree
from tempfile import mkdtemp
from typing import TYPE_CHECKING

import pytest
from sqlalchemy import create_engine

from tests.model import Base

if TYPE_CHECKING:
    from collections.abc import Iterable

    from sqlalchemy.engine import Engine


@pytest.fixture(name="sqlite_engine", scope="session")
def get_sqlite_engine() -> Iterable[Engine]:
    temp_directory: str = mkdtemp()
    engine: Engine = create_engine(f"sqlite:///{temp_directory}/.sqlite")
    Base.metadata.create_all(engine)
    yield engine
    rmtree(temp_directory, ignore_errors=True)
