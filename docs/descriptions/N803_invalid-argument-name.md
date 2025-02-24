# invalid-argument-name (N803)
Derived from the pep8-naming linter.
## What it does
Checks for argument names that do not follow the snake_case convention.
## Why is this bad?
PEP 8 recommends that function names should be lower case and separated
by underscores (also known as snake_case).
Function names should be lowercase, with words separated by underscores
as necessary to improve readability.
Variable names follow the same convention as function names.
mixedCase is allowed only in contexts where that’s already the
prevailing style (e.g. threading.py), to retain backwards compatibility.
In preview, overridden methods are ignored.
## Example
```
def my_function(A, myArg):
    pass
```
## Use instead:
```
def my_function(a, my_arg):
    pass
```