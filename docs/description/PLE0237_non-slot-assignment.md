# non-slot-assignment (PLE0237)
Derived from the Pylint linter.
## What it does
Checks for assignments to attributes that are not defined in __slots__.
## Why is this bad?
When using __slots__, only the specified attributes are allowed.
Attempting to assign to an attribute that is not defined in __slots__
will result in an AttributeError at runtime.
Known problems
This rule can't detect __slots__ implementations in superclasses, and
so limits its analysis to classes that inherit from (at most) object.
## Example
```
class Student:
    __slots__ = ("name",)
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname  # [assigning-non-slot]
        self.setup()
    def setup(self):
        pass
```
## Use instead:
```
class Student:
    __slots__ = ("name", "surname")
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.setup()
    def setup(self):
        pass
```