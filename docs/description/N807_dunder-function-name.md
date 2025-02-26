# dunder-function-name (N807)
Derived from the pep8-naming linter.
## What it does
Checks for functions with "dunder" names (that is, names with two
leading and trailing underscores) that are not documented.
## Why is this bad?
PEP 8 recommends that only documented "dunder" methods are used:
..."magic" objects or attributes that live in user-controlled
namespaces. E.g. __init__, __import__ or __file__. Never invent
such names; only use them as documented.
## Example
```
def __my_function__():
    pass
```
## Use instead:
```
def my_function():
    pass
```