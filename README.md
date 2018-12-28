markdown-newtab
===============

[![Build Status](https://travis-ci.org/pehala/markdown-newtab.svg?branch=master)](https://travis-ci.org/pehala/markdown-newtab)
[![PyPI](https://img.shields.io/pypi/v/markdown3-newtab.svg)](https://pypi.python.org/pypi/markdown3-newtab)
![CC0 License](https://img.shields.io/badge/license-CC0-lightgrey.svg)

This extension modifies the HTML output of Python-Markdown to open all
links in a new tab by adding `target="_blank"`. See `run_tests.py` for
example usage.

Updated to work on Markdown 3.0+.

```
pip install markdown3-newtab
```

### Usage

```python
from markdown import Markdown

Markdown(extensions=[NewTabExtension()])
```

or

```python
from markdown import Markdown

Markdown(extensions=[markdown3-newtab])
```