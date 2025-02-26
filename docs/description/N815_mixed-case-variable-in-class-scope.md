# mixed-case-variable-in-class-scope (N815)
Derived from the pep8-naming linter.
## What it does
Checks for class variable names that follow the mixedCase convention.
## Why is this bad?
PEP 8 recommends that variable names should be lower case and separated
by underscores (also known as snake_case).
Function names should be lowercase, with words separated by underscores
as necessary to improve readability.
Variable names follow the same convention as function names.
mixedCase is allowed only in contexts where that’s already the
prevailing style (e.g. threading.py), to retain backwards compatibility.
## Example
```
class MyClass:
    myVariable = "hello"
    another_variable = "world"
```
## Use instead:
```
class MyClass:
    my_variable = "hello"
    another_variable = "world"
```