"""
Unit testers for the fstring_to_format package.
"""
import io
import os
import sys
from fstring_to_format import __file__ as mfile

MPATH = os.path.dirname(mfile)

def main_tester(command):
    """Tester for __main__.py"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    from fstring_to_format.__main__ import main as rtmain
    rtmain(args=command.split(" "))
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()
