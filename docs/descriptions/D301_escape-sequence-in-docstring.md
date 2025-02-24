# escape-sequence-in-docstring (D301)
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for docstrings that include backslashes, but are not defined as
raw string literals.
## Why is this bad?
In Python, backslashes are typically used to escape characters in strings.
In raw strings (those prefixed with an r), however, backslashes are
treated as literal characters.
PEP 257 recommends
the use of raw strings (i.e., r"""raw triple double quotes""") for
docstrings that include backslashes. The use of a raw string ensures that
any backslashes are treated as literal characters, and not as escape
sequences, which avoids confusion.
## Example
```
def foobar():
    """Docstring for foo\bar."""
foobar.__doc__  # "Docstring for foar."
```
## Use instead:
```
def foobar():
    r"""Docstring for foo\bar."""
foobar.__doc__  # "Docstring for foo\bar."
```