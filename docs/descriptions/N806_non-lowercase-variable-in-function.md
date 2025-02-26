# non-lowercase-variable-in-function (N806)
Derived from the pep8-naming linter.
## What it does
Checks for the use of non-lowercase variable names in functions.
## Why is this bad?
PEP 8 recommends that all function variables use lowercase names:
Function names should be lowercase, with words separated by underscores as necessary to
improve readability. Variable names follow the same convention as function names. mixedCase
is allowed only in contexts where that's already the prevailing style (e.g. threading.py),
to retain backwards compatibility.
## Example
```
def my_function(a):
    B = a + 3
    return B
```
## Use instead:
```
def my_function(a):
    b = a + 3
    return b
```