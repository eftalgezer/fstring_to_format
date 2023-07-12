"""
fstring_to_format terminal client
"""
import sys
from .core import formatify

def main(args):
    """Main function"""
    if len(args) < 2:
        print("Path argument is missing")
        return
    formatify(args[1])

if __name__ == "__main__":
    main(sys.argv)
