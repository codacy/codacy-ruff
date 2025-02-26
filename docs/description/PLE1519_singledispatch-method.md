# singledispatch-method (PLE1519)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for methods decorated with @singledispatch.
## Why is this bad?
The @singledispatch decorator is intended for use with functions, not methods.
Instead, use the @singledispatchmethod decorator, or migrate the method to a
standalone function.
## Example
```
from functools import singledispatch
class Class:
    @singledispatch
    def method(self, arg): ...
```
## Use instead:
```
from functools import singledispatchmethod
class Class:
    @singledispatchmethod
    def method(self, arg): ...
Fix safety
This rule's fix is marked as unsafe, as migrating from @singledispatch to
@singledispatchmethod may change the behavior of the code.
```