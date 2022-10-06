"""
Unit testers for the fstring_to_format package.
"""
from __future__ import absolute_import
import io
import sys
from fstring_to_format import __file__ as mfile
from fstring_to_format.core import unique

MPATH = mfile.replace("{0}fstring_to_format{0}__init__.py".format(os.sep), "").replace("fstring_to_formatc", "fstring_to_format")


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
