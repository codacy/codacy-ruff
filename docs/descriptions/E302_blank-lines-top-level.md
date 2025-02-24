# blank-lines-top-level (E302)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing blank lines between top level functions and classes.
## Why is this bad?
PEP 8 recommends exactly two blank lines between top level functions and classes.
The rule respects the lint.isort.lines-after-imports setting when
determining the required number of blank lines between top-level import
statements and function or class definitions for compatibility with isort.
## Example
```
def func1():
    pass
def func2():
    pass
```
## Use instead:
```
def func1():
    pass
def func2():
    pass
Typing stub files (.pyi)
The typing style guide recommends to not use blank lines between classes and functions except to group
them. That's why this rule is not enabled in typing stub files.
```