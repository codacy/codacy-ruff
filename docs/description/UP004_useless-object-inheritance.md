# useless-object-inheritance (UP004)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for classes that inherit from object.
## Why is this bad?
Since Python 3, all classes inherit from object by default, so object can
be omitted from the list of base classes.
## Example
```
class Foo(object): ...
```
## Use instead:
```
class Foo: ...
```