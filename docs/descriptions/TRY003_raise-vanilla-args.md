# raise-vanilla-args (TRY003)
Derived from the tryceratops linter.
## What it does
Checks for long exception messages that are not defined in the exception
class itself.
## Why is this bad?
By formatting an exception message at the raise site, the exception class
becomes less reusable, and may now raise inconsistent messages depending on
where it is raised.
If the exception message is instead defined within the exception class, it
will be consistent across all raise invocations.
This rule is not enforced for some built-in exceptions that are commonly
raised with a message and would be unusual to subclass, such as
NotImplementedError.
## Example
```
class CantBeNegative(Exception):
    pass
def foo(x):
    if x < 0:
        raise CantBeNegative(f"{x} is negative")
```
## Use instead:
```
class CantBeNegative(Exception):
    def __init__(self, number):
        super().__init__(f"{number} is negative")
def foo(x):
    if x < 0:
        raise CantBeNegative(x)
```