# missing-return-type-special-method (ANN204)
Derived from the flake8-annotations linter.
Fix is sometimes available.
## What it does
Checks that "special" methods, like __init__, __new__, and __call__, have
return type annotations.
## Why is this bad?
Type annotations are a good way to document the return types of functions. They also
help catch bugs, when used alongside a type checker, by ensuring that the types of
any returned values, and the types expected by callers, match expectation.
Note that type checkers often allow you to omit the return type annotation for
__init__ methods, as long as at least one argument has a type annotation. To
opt in to this behavior, use the mypy-init-return setting in your pyproject.toml
or ruff.toml file:
[tool.ruff.lint.flake8-annotations]
mypy-init-return = true
## Example
```
class Foo:
    def __init__(self, x: int):
        self.x = x
```
## Use instead:
```
class Foo:
    def __init__(self, x: int) -> None:
        self.x = x
```