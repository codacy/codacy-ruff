# type-comment-in-stub (PYI033)
Derived from the flake8-pyi linter.
## What it does
Checks for the use of type comments (e.g., x = 1  # type: int) in stub
files.
## Why is this bad?
Stub (.pyi) files should use type annotations directly, rather
than type comments, even if they're intended to support Python 2, since
stub files are not executed at runtime. The one exception is # type: ignore.
## Example
```
x = 1  # type: int
```
## Use instead:
```
x: int = 1
```