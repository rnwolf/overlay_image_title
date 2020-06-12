"""This is a Docstring"""
from typing import Tuple, List
import typer
from PIL import Image, ImageFont, ImageDraw, ImageEnhance


app = typer.Typer()

@app.command()
def add_title(
    source_name: str = typer.Option( "input.jpg", "-i", "--input", help="source filename", show_default=True,),
    output_name: str = "output.jpg",
    position: str = "bottom",
    text: str = "Some text.",
    img_fraction: float = 0.75,
    font_name: str = "arial",
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


if __name__ == "__main__":
    """This is the main entry point."""
    app()
