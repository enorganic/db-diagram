from __future__ import annotations

import sys
from pathlib import Path
from subprocess import check_output
from tempfile import mkdtemp
from typing import TYPE_CHECKING

import pytest

from db_diagram import (
    write_markdown,
    write_mermaid_images,
    write_mermaid_markdown,
)

if TYPE_CHECKING:
    from sqlalchemy import Engine

TESTS_DIRECTORY: Path = Path(__file__).absolute().parent
LIB_DATA_DIRECTORY: Path = TESTS_DIRECTORY / "data/lib/sqlite"
CLI_DATA_DIRECTORY: Path = TESTS_DIRECTORY / "data/cli/sqlite"


def _validate_files(directory: Path, reference_directory: Path) -> None:
    """
    Validate that the files in the directory match the reference directory
    """
    path: Path
    files: tuple[Path, ...] = tuple(
        path.relative_to(directory)
        for path in directory.glob("**/*")
        if path.is_file()
    )
    reference_files: tuple[Path, ...] = tuple(
        path.relative_to(reference_directory)
        for path in reference_directory.glob("**/*")
        if path.is_file()
    )
    file_paths: set[str] = set(map(str, files))
    reference_file_paths: set[str] = set(map(str, reference_files))
    assert file_paths == reference_file_paths, (
        f"\n{directory.absolute()!s}\n!=\n"
        f"{reference_directory.absolute()!s}"
    )
    for path in files:
        if path.suffix in (".svg", ".png"):
            # We exclude SVG/PNG files because changes could be introduced
            # by mmdc which are outside our control
            continue
        file: Path = directory.joinpath(path)
        text: str = file.read_text().strip()
        reference_file: Path = reference_directory.joinpath(path)
        reference_text: str = reference_file.read_text().strip()
        assert text == reference_text, (
            f"\n{file}\n"
            "!=\n"
            f"{reference_file}\n\n"
            f"{text}\n"
            "!=\n"
            f"{reference_text}"
        )


def test_sqlite(sqlite_engine: Engine) -> None:
    """
    Generate mermaid diagrams and compare the output with previously
    generated diagrams
    """
    directory: Path
    if tuple(LIB_DATA_DIRECTORY.glob("**/*")):
        # If test files exist, we'll write our output to a temp directory
        directory = Path(mkdtemp())
    else:
        # If test files don't exist, we'll save our output as the test files
        # to be used for validating future runs
        directory = LIB_DATA_DIRECTORY
    # sqlite
    # Write diagrams with a depth of 1
    depth: int
    for depth in range(1, 4):
        write_mermaid_markdown(
            sqlite_engine,
            directory=directory / f"depth={depth}/mmd",
            depth=depth,
        )
        write_mermaid_images(
            sqlite_engine,
            directory=directory / f"depth={depth}/svg",
            depth=depth,
            format_="svg",
            theme="dark",
        )
        write_mermaid_images(
            sqlite_engine,
            directory=directory / f"depth={depth}/png",
            depth=depth,
            format_="png",
        )
        write_markdown(
            sqlite_engine,
            path=directory / f"depth={depth}/diagrams.md",
            depth=depth,
        )
        write_markdown(
            sqlite_engine,
            path=directory / f"depth={depth}/diagrams_svg.md",
            depth=depth,
            image_directory=directory / f"depth={depth}/svg",
            image_format="svg",
        )
        write_markdown(
            sqlite_engine,
            path=directory / f"depth={depth}/diagrams_png.md",
            depth=depth,
            image_directory=directory / f"depth={depth}/png",
            image_format="png",
        )
    # Verify the new/old files are the same
    if directory is not LIB_DATA_DIRECTORY:
        _validate_files(directory, LIB_DATA_DIRECTORY)


def test_cli_sqlite(sqlite_engine: Engine) -> None:
    """
    Generate mermaid diagrams using the CLI and compare the output with
    previously generated diagrams
    """
    directory: Path
    if tuple(CLI_DATA_DIRECTORY.glob("**/*")):
        # If test files exist, we'll write our output to a temp directory
        directory = Path(mkdtemp())
    else:
        # If test files don't exist, we'll save our output as the test files
        # to be used for validating future runs
        directory = CLI_DATA_DIRECTORY
    # sqlite
    # Write diagrams with a depth of 1
    depth: str
    for depth in map(str, range(1, 4)):
        url: str = str(sqlite_engine.url)
        check_output(
            (
                sys.executable,
                "-m",
                "db_diagram",
                url,
                "-d",
                depth,
                "-mmd",
                str(directory / f"depth={depth}/mmd"),
                "-svg",
                str(directory / f"depth={depth}/svg"),
                "-md",
                str(directory / f"depth={depth}/diagrams_svg.md"),
            )
        )
        check_output(
            (
                sys.executable,
                "-m",
                "db_diagram",
                url,
                "-d",
                depth,
                "-mmd",
                str(directory / f"depth={depth}/mmd"),
                "-png",
                str(directory / f"depth={depth}/png"),
                "-md",
                str(directory / f"depth={depth}/diagrams_png.md"),
            )
        )
        check_output(
            (
                sys.executable,
                "-m",
                "db_diagram",
                url,
                "-d",
                "1",
                "-md",
                str(directory / f"depth={depth}/diagrams.md"),
            )
        )


if __name__ == "__main__":
    pytest.main(["-s", "-vv", __file__])
