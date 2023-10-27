"""test main module
"""

import sys

sys.path.append("src")

from main import hello_world


def test_main():
    """test main function"""
    assert hello_world() == "hello world!"
