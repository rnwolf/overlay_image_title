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


def assert_images_equal(image_1: str, image_2: str):
    img1 = Image.open(image_1)
    img2 = Image.open(image_2)

    # Convert to same mode and size for comparison
    img2 = img2.convert(img1.mode)
    img2 = img2.resize(img1.size)

    sum_sq_diff = np.sum((np.asarray(img1).astype('float') - np.asarray(img2).astype('float'))**2)

    if sum_sq_diff == 0:
        # Images are exactly the same
        pass
    else:
        normalized_sum_sq_diff = sum_sq_diff / np.sqrt(sum_sq_diff)
        assert normalized_sum_sq_diff < 0.001


@pytest.fixture
def image_similarity(request, tmpdir):
    testname = request.node.name
    filename = "{}.png".format(testname)
    generated_file = os.path.join(str(tmpdir), "{}.png".format(testname))

    yield {'filename': generated_file}

    assert_images_equal("tests/baseline_images/{}.png".format(testname), generated_file)
