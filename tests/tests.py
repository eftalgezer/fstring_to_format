"""
Unit tests for the fstring_to_format package.
"""
from __future__ import absolute_import
import os
from fstring_to_format import __file__ as mfile
from .testers import main_tester

MPATH = mfile.replace("/fstring_to_format/__init__.py", "")

def test_main():
    """Tests for __main__.py"""
    os.chdir(f"{MPATH}{os.sep}tests{os.sep}assets")
    assert "All files are converted" in main_tester("fstring_to_format file1.py.test")
