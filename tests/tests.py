"""
Unit tests for the fstring_to_format package.
"""
import os
from fstring_to_format import __file__ as mfile
from .testers import main_tester

MPATH = os.path.dirname(mfile)

def test_main():
    """Tests for __main__.py"""
    os.chdir(os.path.join("tests", "assets"))
    assert "All files are converted" in main_tester("fstring_to_format file*.py.test")
    assert "No files are found" in main_tester("fstring_to_format Foo.py.test")
