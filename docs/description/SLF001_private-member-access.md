# private-member-access (SLF001)
Derived from the flake8-self linter.
## What it does
Checks for accesses on "private" class members.
## Why is this bad?
In Python, the convention is such that class members that are prefixed
with a single underscore, or prefixed but not suffixed with a double
underscore, are considered private and intended for internal use.
Using such "private" members is considered a misuse of the class, as
there are no guarantees that the member will be present in future
versions, that it will have the same type, or that it will have the same
behavior. Instead, use the class's public interface.
This rule ignores accesses on dunder methods (e.g., __init__) and sunder
methods (e.g., _missing_).
## Example
```
class Class:
    def __init__(self):
        self._private_member = "..."
var = Class()
print(var._private_member)
```
## Use instead:
```
class Class:
    def __init__(self):
        self.public_member = "..."
var = Class()
print(var.public_member)
```