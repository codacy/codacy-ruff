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
Fix safety
This rule's fix is marked as unsafe if there's comments in the
base classes, as comments may be removed.
For example, the fix would be marked as unsafe in the following case:
class Foo:
    pass
class Bar(
    Foo,  # comment
    Foo,
):
    pass
```