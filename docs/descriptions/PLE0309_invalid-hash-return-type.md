# invalid-hash-return-type (PLE0309)
Derived from the Pylint linter.
## What it does
Checks for __hash__ implementations that return non-integer values.
## Why is this bad?
The __hash__ method should return an integer. Returning a different
type may cause unexpected behavior.
Note: bool is a subclass of int, so it's technically valid for __hash__ to
return True or False. However, for consistency with other rules, Ruff will
still emit a diagnostic when __hash__ returns a bool.
## Example
```
class Foo:
    def __hash__(self):
        return "2"
```
## Use instead:
```
class Foo:
    def __hash__(self):
        return 2
```