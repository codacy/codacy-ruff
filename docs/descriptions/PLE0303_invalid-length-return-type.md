# invalid-length-return-type (PLE0303)
Derived from the Pylint linter.
## What it does
Checks for __len__ implementations that return values that are not non-negative
integers.
## Why is this bad?
The __len__ method should return a non-negative integer. Returning a different
value may cause unexpected behavior.
Note: bool is a subclass of int, so it's technically valid for __len__ to
return True or False. However, for consistency with other rules, Ruff will
still emit a diagnostic when __len__ returns a bool.
## Example
```
class Foo:
    def __len__(self):
        return "2"
```
## Use instead:
```
class Foo:
    def __len__(self):
        return 2
```