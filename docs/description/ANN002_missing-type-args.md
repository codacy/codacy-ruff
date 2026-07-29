# missing-type-args (ANN002)
Added in v0.0.105 ·
Related issues ·
View source
Derived from the flake8-annotations linter.
## What it does
Checks that function *args arguments have type annotations.
## Why is this bad?
Type annotations are a good way to document the types of function arguments. They also
help catch bugs, when used alongside a type checker, by ensuring that the types of
any provided arguments match expectation.
## Example
```
def foo(*args): ...
```
## Use instead:
```
def foo(*args: int): ...
```