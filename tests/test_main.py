"""test main module
"""
import sys

from main import hello_world

sys.path.append("src")


def test_main():
    """test main function"""
    assert hello_world() == "hello world!"
