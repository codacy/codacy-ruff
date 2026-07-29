# legacy-type-comment (PYI033)
Added in v0.0.254 ·
Related issues ·
View source
Derived from the flake8-pyi linter.
## What it does
Checks for the use of type comments (e.g., x = 1  # type: int).
By default, this check only runs on stub files. If preview mode is enabled,
the check also runs on .py files.
## Why is this bad?
Type comments are a soft-deprecated form of type annotation. They are unsupported
by some modern type checkers, including ty and Pyrefly, and are only necessary when
supporting end-of-life Python versions such as 3.5 or older. They are never necessary
in stub files, which are not executed at runtime.
This rule does not apply to # type: ignore suppression comments.
## Example
```
x = 1  # type: int
```
## Use instead:
```
x: int = 1
```