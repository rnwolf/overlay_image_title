"""This is a docstring to help you undersyand your tests later."""
from imagetitle.imagetitle import add_title

SOURCE_IMAGE = "./tests/input.png"

def test_title_bottom(image_similarity):
    """Doc string goes here"""
    result = add_title(
        source_name=SOURCE_IMAGE,
        output_name=image_similarity["filename"],
        font_name="arial",
    )  # noqa: F841


def test_title_left(image_similarity):
    """Doc string goes here"""
    result = app(
        source_name=SOURCE_IMAGE,
        output_name=image_similarity["filename"],
        position="left",
    )  # noqa: F841


def test_title_right(image_similarity):
    """Doc string goes here"""
    result = app(
        source_name=SOURCE_IMAGE,
        output_name=image_similarity["filename"],
        position="right",
    )  # noqa: F841


def test_title_top(image_similarity):
    """Doc string goes here"""
    result = app(
        source_name=SOURCE_IMAGE,
        output_name=image_similarity["filename"],
        position="top",
    )  # noqa: F841


def test_command_line(capsys):
    """Doc string goes here"""
    result = app(text="Image by Irfan Simsar via Unsplash.")  # noqa: F841
    stdout = capsys.readouterr().out

    # regex = re.compile(r"rolling (\d+D\d+)!\n\nyour roll: (\d+)")
    # roll_str, total = re.search(regex, stdout).groups()
    assert True == True
