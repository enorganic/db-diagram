from __future__ import annotations

from subprocess import check_call


def test_install_npm() -> None:
    """
    Test that npm can be installed.
    """
    from db_diagram._mermaid import install_npm

    npm: str = install_npm(force=True)
    check_call((npm, "--version"))
