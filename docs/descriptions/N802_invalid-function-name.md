# invalid-function-name (N802)
Derived from the pep8-naming linter.
## What it does
Checks for functions names that do not follow the snake_case naming
convention.
## Why is this bad?
PEP 8 recommends that function names follow snake_case:
Function names should be lowercase, with words separated by underscores as necessary to
improve readability. mixedCase is allowed only in contexts where that’s already the
prevailing style (e.g. threading.py), to retain backwards compatibility.
Names can be excluded from this rule using the lint.pep8-naming.ignore-names
or lint.pep8-naming.extend-ignore-names configuration options. For example,
to ignore all functions starting with test_ from this rule, set the
lint.pep8-naming.extend-ignore-names option to ["test_*"].
## Example
```
def myFunction():
    pass
```
## Use instead:
```
def my_function():
    pass
```