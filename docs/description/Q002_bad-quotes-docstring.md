# bad-quotes-docstring (Q002)
Derived from the flake8-quotes linter.
Fix is sometimes available.
## What it does
Checks for docstrings that use single quotes or double quotes, depending
on the value of the lint.flake8-quotes.docstring-quotes setting.
## Why is this bad?
Consistency is good. Use either single or double quotes for docstring
strings, but be consistent.
## Example
```
'''
bar
'''
Assuming docstring-quotes is set to double, use instead:
"""
bar
"""
```