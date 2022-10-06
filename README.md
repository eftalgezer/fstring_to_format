# fstring_to_format
[![PyPI version](https://badge.fury.io/py/fstring_to_format.svg)](https://badge.fury.io/py/fstring_to_format)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/fstring_to_format.svg)](https://pypi.python.org/pypi/fstring_to_format/)
[![Python package](https://github.com/eftalgezer/fstring_to_format/actions/workflows/python-package.yml/badge.svg)](https://github.com/eftalgezer/fstring_to_format/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/eftalgezer/fstring_to_format/branch/main/graph/badge.svg?token=Q9TJFIN1U1)](https://codecov.io/gh/eftalgezer/fstring_to_format)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/3bec71a96f374f24b26b077619350f30)](https://www.codacy.com/gh/eftalgezer/fstring_to_format/dashboard?utm_source=github.com&utm_medium=referral&utm_content=eftalgezer/fstring_to_format&utm_campaign=Badge_Coverage)
[![PyPI download month](https://img.shields.io/pypi/dm/fstring_to_format.svg)](https://pypi.python.org/pypi/fstring_to_format/)
[![PyPI download week](https://img.shields.io/pypi/dw/fstring_to_format.svg)](https://pypi.python.org/pypi/fstring_to_format/)
[![PyPI download day](https://img.shields.io/pypi/dd/fstring_to_format.svg)](https://pypi.python.org/pypi/fstring_to_format/)
![GitHub all releases](https://img.shields.io/github/downloads/eftalgezer/fstring_to_format/total?style=flat)
[![GitHub contributors](https://img.shields.io/github/contributors/eftalgezer/fstring_to_format.svg)](https://github.com/eftalgezer/fstring_to_format/graphs/contributors/)
[![CodeFactor](https://www.codefactor.io/repository/github/eftalgezer/fstring_to_format/badge)](https://www.codefactor.io/repository/github/eftalgezer/fstring_to_format)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3bec71a96f374f24b26b077619350f30)](https://www.codacy.com/gh/eftalgezer/fstring_to_format/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=eftalgezer/fstring_to_format&amp;utm_campaign=Badge_Grade)
[![PyPI license](https://img.shields.io/pypi/l/fstring_to_format.svg)](https://pypi.python.org/pypi/fstring_to_format/)

fstring_to_format converts Python f-string expressions to .format() for backwards compatibility. 

There are other packages for this too, but this is a regular expression based cleaner solution.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install fstring_to_format.

```bash
$ pip install fstring_to_format

# to make sure you have the latest version
$ pip install -U fstring_to_format

# latest available code base
$ pip install -U git+https://github.com/eftalgezer/fstring_to_format.git
```

## Usage

```bash
$ python -m fstring_to_format filename.py # for a single file
$ python -m fstring_to_format *.py # for all Python files in a directory
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU General Public License v3.0](https://github.com/eftalgezer/fstring_to_format/blob/master/LICENSE) 
 
