"""
Unit tests for the fstring_to_format package.
"""
import os
from fstring_to_format import __file__ as mfile
from .testers import main_tester

MPATH = mfile.replace("{0}fstring_to_format{0}__init__.py".format(os.sep), "").replace("fstring_to_formatc", "fstring_to_format")

def test_main():
    """Tests for __main__.py"""
    os.chdir(os.path.join(MPATH, "tests", "assets"))
    assert "All files are converted" in main_tester("fstring_to_format file*.py.test")
    assert "No files are found" in main_tester("fstring_to_format Foo.py.test")
