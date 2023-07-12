import sys
from .core import formatify

def main():
    """Main function"""
    if len(sys.argv) < 2:
        print("Path argument is missing")
        return
    formatify(sys.argv[1])

if __name__ == "__main__":
    main()