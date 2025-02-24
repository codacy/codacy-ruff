# invalid-index-return-type (PLE0305)
Derived from the Pylint linter.
## What it does
Checks for __index__ implementations that return non-integer values.
## Why is this bad?
The __index__ method should return an integer. Returning a different
type may cause unexpected behavior.
Note: bool is a subclass of int, so it's technically valid for __index__ to
return True or False. However, a DeprecationWarning (DeprecationWarning: __index__ returned non-int (type bool)) for such cases was already introduced,
thus this is a conscious difference between the original pylint rule and the
current ruff implementation.
## Example
```
class Foo:
    def __index__(self):
        return "2"
```
## Use instead:
```
class Foo:
    def __index__(self):
        return 2
```