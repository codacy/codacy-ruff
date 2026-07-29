# raise-not-implemented (F901)
Added in v0.0.18 ·
Related issues ·
View source
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for raise statements that raise NotImplemented.
## Why is this bad?
NotImplemented is a special value returned by binary special methods to indicate
that an operation is not implemented with respect to a particular type.
Because NotImplemented is not an exception, it cannot be raised.
Raise NotImplementedError instead, which is used to indicate that a method is
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