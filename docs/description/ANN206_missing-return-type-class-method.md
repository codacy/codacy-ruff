# missing-return-type-class-method (ANN206)
Derived from the flake8-annotations linter.
Fix is sometimes available.
## What it does
Checks that class methods have return type annotations.
## Why is this bad?
Type annotations are a good way to document the return types of functions. They also
help catch bugs, when used alongside a type checker, by ensuring that the types of
any returned values, and the types expected by callers, match expectation.
## Example
```
class Foo:
    @classmethod
    def bar(cls):
        return 1
```
## Use instead:
```
class Foo:
    @classmethod
    def bar(cls) -> int:
        return 1
```