# raise-not-implemented (F901)
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for raise statements that raise NotImplemented.
## Why is this bad?
NotImplemented is an exception used by binary special methods to indicate
that an operation is not implemented with respect to a particular type.
NotImplemented should not be raised directly. Instead, raise
NotImplementedError, which is used to indicate that the method is
abstract or not implemented in the derived class.
## Example
```
class Foo:
    def bar(self):
        raise NotImplemented
```
## Use instead:
```
class Foo:
    def bar(self):
        raise NotImplementedError
```