# missing-return-type-undocumented-public-function (ANN201)
Derived from the flake8-annotations linter.
Fix is sometimes available.
## What it does
Checks that public functions and methods have return type annotations.
## Why is this bad?
Type annotations are a good way to document the return types of functions. They also
help catch bugs, when used alongside a type checker, by ensuring that the types of
any returned values, and the types expected by callers, match expectation.
## Example
```
def add(a, b):
    return a + b
```
## Use instead:
```
def add(a: int, b: int) -> int:
    return a + b
```