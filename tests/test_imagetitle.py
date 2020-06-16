"""This is a docstring to help you undersyand your tests later."""
from typer.testing import CliRunner
from imagetitle.imagetitle import app, main
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
    fonts = {'posix': 'Times New Roman',
             'Windows': 'arial',
             'Darwin': 'Times'}
    return fonts[osname]


def test_app():
    """Doc string goes here"""
    result = runner.invoke(app, ["World"])
    assert result.exit_code == 0
    assert "World" in result.stdout


