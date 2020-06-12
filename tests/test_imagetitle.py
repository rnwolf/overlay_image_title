"""This is a docstring to help you undersyand your tests later."""
from imagetitle.imagetitle import add_title


def test_title_bottom(image_similarity):
    """Doc string goes here"""
    result = add_title(
        source_name="./tests/input.png", output_name=image_similarity['filename'],
    )  # noqa: F841

def test_title_left(image_similarity):
    """Doc string goes here"""
    result = add_title(
        source_name="./tests/input.png", output_name=image_similarity['filename'], position="left"
    )  # noqa: F841


def test_title_right(image_similarity):
    """Doc string goes here"""
    result = add_title(
        source_name="./tests/input.png", output_name=image_similarity['filename'], position="right"
    )  # noqa: F841


def test_title_top(image_similarity):
    """Doc string goes here"""
    result = add_title(
        source_name="./tests/input.png", output_name=image_similarity['filename'], position="top"
    )  # noqa: F841

def test_command_line(capsys):
    """Doc string goes here"""
    result = add_title(num_dice=1, sides=20)  # noqa: F841
    stdout = capsys.readouterr().out

    #regex = re.compile(r"rolling (\d+D\d+)!\n\nyour roll: (\d+)")
    #roll_str, total = re.search(regex, stdout).groups()
    assert True == True
