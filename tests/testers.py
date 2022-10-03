"""
Unit testers for the fstring_to_format package.
"""
from __future__ import absolute_import
import io
import sys
from fstring_to_format import __file__ as mfile

MPATH = mfile.replace("/fstring_to_format/__init__.py", "")


def main_tester(command):
    """Tester for __main__.py"""
    capturedoutput = io.StringIO()
    sys.stdout = capturedoutput
    from fstring_to_format.__main__ import main as rtmain
    rtmain(args=command.split(" "))
    sys.stdout = sys.__stdout__
    return capturedoutput.getvalue()
