from mitmproxy.contentviews import image
from mitmproxy.test import tutils
from . import full_eval


def test_view_image():
    v = full_eval(image.ViewImage())
    for img in [
        "mitmproxy/data/image.png",
        "mitmproxy/data/image.gif",
        "mitmproxy/data/all.jpeg",
        "mitmproxy/data/image.ico"
    ]:
        with open(tutils.test_data.path(img), "rb") as f:
            assert v(f.read())

    assert not v(b"flibble")
