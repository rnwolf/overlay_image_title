"""
For pytest.

By defining conftest.py in your root path, pytest will recognize application
modules without specifying PYTHONPATH.
In the background, py.test modifies your sys.path by including all
submodules which are found from the root path.

"""
import os
import pytest
import numpy as np
from PIL import Image
import platform
from diffimg import diff

def assert_images_equal(image_1: str, image_2: str):
    """ Compare if two PNG images are nearly similar. """
    #img1 = Image.open(image_1)
    #img2 = Image.open(image_2)

    # Convert to same mode and size for comparison
    #img2 = img2.convert(img1.mode)
    #img2 = img2.resize(img1.size)

    #sum_sq_diff = np.sum(
    #    (np.asarray(img1).astype("float") - np.asarray(img2).astype("float")) ** 2,
    #)
    percent_diff = diff(image_1,image_2,delete_diff_file=True,ignore_alpha=False)

    if percent_diff <= 5.0:
        # Images are almost the same
        pass
    else:
        #normalized_sum_sq_diff = sum_sq_diff / np.sqrt(sum_sq_diff)
        #assert normalized_sum_sq_diff < 0.001
        assert percent_diff < 5.0


@pytest.fixture
def image_similarity(request, tmpdir):
    """ Use this Fixture to test if generated images equals saved baseline images.
    """
    testname = request.node.name
    osname = platform.system()  # 'posix', 'Windows' or 'Darwin'
    filename = f"{testname}_{osname}.png"  # noqa: F841
    generated_file = os.path.join(str(tmpdir), f"{testname}_{osname}.png")

    yield {"filename": generated_file}

    assert_images_equal(
        f"tests/baseline_images/{testname}_{osname}.png", generated_file,
    )
