# import-self (PLW0406)
Derived from the Pylint linter.
## What it does
Checks for import statements that import the current module.
## Why is this bad?
Importing a module from itself is a circular dependency and results
in an ImportError exception.
## Example
```
# file: this_file.py
from this_file import foo
def foo(): ...
```