# invalid-bytes-return-type (PLE0308)
Added in 0.6.0 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for __bytes__ implementations that return types other than bytes.
## Why is this bad?
The __bytes__ method should return a bytes object. Returning a different
type may cause unexpected behavior.
## Example
```
class Foo:
    def __bytes__(self):
        return 2
```
## Use instead:
```
class Foo:
    def __bytes__(self):
        return b"2"
```