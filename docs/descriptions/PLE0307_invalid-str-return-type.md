# invalid-str-return-type (PLE0307)
Derived from the Pylint linter.
## What it does
Checks for __str__ implementations that return a type other than str.
## Why is this bad?
The __str__ method should return a str object. Returning a different
type may cause unexpected behavior.
## Example
```
class Foo:
    def __str__(self):
        return True
```
## Use instead:
```
class Foo:
    def __str__(self):
        return "Foo"
```