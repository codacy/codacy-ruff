# useless-metaclass-type (UP001)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for the use of __metaclass__ = type in class definitions.
## Why is this bad?
Since Python 3, __metaclass__ = type is implied and can thus be omitted.
## Example
```
class Foo:
    __metaclass__ = type
```
## Use instead:
```
class Foo: ...
```