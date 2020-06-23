"""This is a docstring to help you undersyand your tests later."""
from typer.testing import CliRunner
from imagetitle.imagetitle import app
import platform

runner = CliRunner()

SOURCE_IMAGE = "./tests/input.png"


def get_os_font():
    """The fonts installed on each OS differ.
    So when generating images with text on each OS
    we need to specify specific fonts that are going to be there.

    See: https://fontsarena.com/blog/operating-systems-default-serif-fonts/

    """
    osname = platform.system()  # 'posix', 'Windows' or 'Darwin'
    fonts = {"Linux": "Ubuntu-C.ttf", "Windows": "Ubuntu-C.ttf", "Darwin": "Times"}
    return fonts[osname]


def test_version():
    """Doc string goes here"""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "Version" in result.stdout


def test_app_input_not_valid():
    """Doc string goes here"""
    result = runner.invoke(app, ["-i", "file-does-not-exist.png"])
    assert result.exit_code == 2
    # assert "World" in result.stdout


def test_app_input_image_not_valid():
    """Doc string goes here"""
    result = runner.invoke(app, ["-i", "./tests/test_icon_image.ico"])
    assert result.exit_code == 2
    assert "not a suitable image file" in result.stdout


def test_app__position_not_valid():
    """Doc string goes here"""
    result = runner.invoke(app, ["-p", "this-is-not-a-valid-position"])
    assert result.exit_code == 2


def test_app_position_top(image_similarity):
    """Doc string goes here"""
    result = runner.invoke(
        app, ["-p", "top", "-f", get_os_font(), "-o", image_similarity["filename"]],
    )
    assert result.exit_code == 0


def test_app_position_bottom(image_similarity):
    """Doc string goes here"""
    result = runner.invoke(
        app, ["-p", "bottom", "-f", get_os_font(), "-o", image_similarity["filename"]],
    )
    assert result.exit_code == 0


def test_app_position_left(image_similarity):
    """Doc string goes here"""
    result = runner.invoke(
        app, ["-p", "left", "-f", get_os_font(), "-o", image_similarity["filename"]],
    )
    assert result.exit_code == 0


def test_app_position_right(image_similarity):
    """Doc string goes here"""
    result = runner.invoke(
        app, ["-p", "right", "-f", get_os_font(), "-o", image_similarity["filename"]],
    )
    assert result.exit_code == 0


def test_img_fraction():
    """Doc string goes here"""
    result = runner.invoke(app, ["-r", "0.8"])
    assert result.exit_code == 0


def test_img_fraction_to_big():
    """Doc string goes here"""
    result = runner.invoke(app, ["-r", "1.8"])
    assert result.exit_code == 2


def test_font_exists():
    """Doc string goes here"""
    result = runner.invoke(app, ["-f", get_os_font()])
    assert result.exit_code == 0


def test_font_does_not_exists():
    """Doc string goes here"""
    result = runner.invoke(app, ["-f", "This font does not exist"])
    assert result.exit_code == 2


def test_app_with_defaults():
    """ Run test with all the default values."""
    result = runner.invoke(app, [])
    assert result.exit_code == 0
