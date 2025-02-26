# error-suffix-on-exception-name (N818)
Derived from the pep8-naming linter.
## What it does
Checks for custom exception definitions that omit the Error suffix.
## Why is this bad?
The Error suffix is recommended by PEP 8:
Because exceptions should be classes, the class naming convention
applies here. However, you should use the suffix "Error" on your
exception names (if the exception actually is an error).
## Example
```
class Validation(Exception): ...
```
## Use instead:
```
class ValidationError(Exception): ...
```