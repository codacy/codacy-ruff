# duplicate-bases (PLE0241)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for duplicate base classes in class definitions.
## Why is this bad?
Including duplicate base classes will raise a TypeError at runtime.
## Example
```
class Foo:
    pass
class Bar(Foo, Foo):
    pass
```
## Use instead:
```
class Foo:
    pass
class Bar(Foo):
    pass
```