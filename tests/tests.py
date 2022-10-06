"""
Unit tests for the fstring_to_format package.
"""
from __future__ import absolute_import
import os
from fstring_to_format import __file__ as mfile
from .testers import main_tester, unique_tester

MPATH = mfile.replace("/fstring_to_format/__init__.py", "").replace("fstring_to_formatc", "fstring_to_format")


def test_main():
    """Tests for __main__.py"""
    os.chdir("{0}{1}tests{1}assets".format(MPATH, os.sep))
    assert "All files are converted" in main_tester("fstring_to_format file*.py.test")
    assert "No files are found" in main_tester("fstring_to_format Foo.py.test")


def test_unique():
    assert unique_tester(["{mpath}", "{mpath}", "{os.sep}", "{os.sep}"]) == ["{mpath}", "{os.sep}"]
