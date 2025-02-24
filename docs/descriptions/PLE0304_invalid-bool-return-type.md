# invalid-bool-return-type (PLE0304)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for __bool__ implementations that return a type other than bool.
## Why is this bad?
The __bool__ method should return a bool object. Returning a different
type may cause unexpected behavior.
## Example
```
class Foo:
    def __bool__(self):
        return 2
```
## Use instead:
```
class Foo:
    def __bool__(self):
        return True
```