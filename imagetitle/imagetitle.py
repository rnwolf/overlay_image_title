"""This is a Docstring"""
from typing import Tuple, List
import typer
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
from pathlib import Path
from enum import Enum

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


app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"Version: {__version__}")
        raise typer.Exit()


@app.command()
def add_title(
    source_name: Path = typer.Argument()   Option(
        "input.png", "-i", "--input", help="source filename", show_default=True,
    ),
    output_name: Path = typer.Option(
        "output.png", "-o", "--output", help="output filename", show_default=True,
    ),
    position: TitlePosition = typer.Option(
        TitlePosition.bottom,
        "-p",
        "--position",
        help="where to position the title on the image.",
        show_default=True,
    ),
    text: str = typer.Option("Some text.", "-t", "--text", help="Title text",),
    img_fraction: float = typer.Option(
        0.75,
        min=0,
        max=1,
        help="A faction between 0 and 1, specifying proportion of the edge title should cover.",
        show_default=True,
    ),
    font_name: str = typer.Option(
        "arial",
        "-f",
        "--font",
        help="The font name for the title text.",
        show_default=True,
    ),
    version: bool = typer.Option(None, "--version", callback=version_callback),
):
    typer.echo("hello")
    source_img = Image.open(source_name)
    image_format = source_img.format
    source_img = source_img.convert("RGBA")
    width, hight = source_img.size

    fontsize = 1  # starting font size
    font = ImageFont.truetype(font_name, fontsize)
    breakpoint = img_fraction * source_img.size[0]
    jumpsize = 75
    while True:
        if font.getsize(text)[0] < breakpoint:
            fontsize += jumpsize
        else:
            jumpsize = int(jumpsize / 2)
            fontsize -= jumpsize
        font = ImageFont.truetype(font_name, fontsize)
        if jumpsize <= 1:
            break

    # get text size
    text_size = font.getsize(text)

    # set button size + 10px margins
    button_size = (text_size[0] + 20, text_size[1] + 20)

    # create image with correct size and black background
    button_img = Image.new("RGBA", button_size, "grey")

    # put text on button with 10px margins
    button_draw = ImageDraw.Draw(button_img)
    button_draw.text((10, 10), text, font=font)

    # put button on source image in position (0, 0)
    if position == "bottom":
        source_img.paste(button_img, (0, hight - button_size[1]))
    elif position == "top":
        source_img.paste(button_img, (0, 0))
    elif position == "right":
        transposed_img = button_img.transpose(Image.ROTATE_270)
        source_img.paste(transposed_img, (width - button_size[1], 0))
    elif position == "left":
        transposed_img = button_img.transpose(Image.ROTATE_90)
        source_img.paste(transposed_img, (0, hight - button_size[0]))

    # save in new file
    source_img.convert("RGB").save(output_name, image_format)
