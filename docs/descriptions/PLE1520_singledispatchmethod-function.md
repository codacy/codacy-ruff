# singledispatchmethod-function (PLE1520)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for non-method functions decorated with @singledispatchmethod.
## Why is this bad?
The @singledispatchmethod decorator is intended for use with methods, not
functions.
Instead, use the @singledispatch decorator.
## Example
```
from functools import singledispatchmethod
@singledispatchmethod
def func(arg): ...
```
## Use instead:
```
from functools import singledispatch
@singledispatch
def func(arg): ...
Fix safety
This rule's fix is marked as unsafe, as migrating from @singledispatchmethod to
@singledispatch may change the behavior of the code.
```