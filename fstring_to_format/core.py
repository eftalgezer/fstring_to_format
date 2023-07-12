
"""
Module bundling all functions needed to convert f-strings to .format()
"""
from __future__ import print_function
from __future__ import unicode_literals
import re
import glob
import shutil
import io
import os

MAINPATTERN = re.compile(r"f['\"].*\{[^\{\s}]+\}+.*['\"]")
PARTPATTERN = re.compile(r"\{[^\{\}\s]+\}")

def formatify(path):
    files = glob.glob(path)
    files = [file for file in files if os.path.isfile(file)]
    if not files:
        print("No files are found")
        return
    for file in files:
        print("Backing up {0}".format(file))
        shutil.copy(file, "{0}.temp".format(file))
        with io.open(file, "r+", encoding="utf-8") as f:
            print("Opening {0}".format(file))
            content = f.read()
            matches = MAINPATTERN.findall(content)
            for match in matches:
                parts = PARTPATTERN.findall(match)
                unique_parts = []
                [unique_parts.append(part) for part in parts if part not in unique_parts]
                toreplace = match
                for ind, part in enumerate(unique_parts):
                    toreplace = toreplace.replace(part, "{" + str(ind) + "}").lstrip("f")
                toreplace += ".format(" + ', '.join(unique_parts) + ')'
                content = content.replace(match, toreplace)
            f.seek(0)
            f.truncate(0)
            print("Writing {0}".format(file))
            f.write(content)
    print("All files are converted")