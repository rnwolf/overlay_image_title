"""This is a Docstring"""
from typing import Tuple, List
import typer
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from pathlib import Path
from enum import Enum

app = typer.Typer()

try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError


try:
    __version__ = version("imagetitle")
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"


class TitlePosition(str, Enum):
    bottom = "bottom"
    top = "top"
    left = "left"
    right = "right"


def version_callback(value: bool):
    if value:
        typer.echo(f"Version: {__version__}")
        raise typer.Exit()


@app.command()
def main(
    name: str,
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    """[summary]

    Args:
        version (bool, optional): [description]. Defaults to typer.Option(None, "--version", callback=version_callback).
    """
    typer.echo(f"hello {name}.")
