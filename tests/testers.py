"""
Unit testers for the fstring_to_format package.
"""
import io
import os
import sys
from fstring_to_format import __file__ as mfile
from fstring_to_format.core import unique

MPATH = os.path.dirname(mfile)

def main_tester(command):
    """Tester for __main__.py"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    from fstring_to_format.__main__ import main as rtmain
    rtmain(args=command.split(" "))
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()

def unique_tester(list1):
    """Tester function for unique"""
    return unique(list1)
