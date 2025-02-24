# redefined-slots-in-subclass (PLW0244)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for a re-defined slot in a subclass.
## Why is this bad?
If a class defines a slot also defined in a base class, the
instance variable defined by the base class slot is inaccessible
(except by retrieving its descriptor directly from the base class).
## Example
```
class Base:
    __slots__ = ("a", "b")
class Subclass(Base):
    __slots__ = ("a", "d")  # slot "a" redefined
```
## Use instead:
```
class Base:
    __slots__ = ("a", "b")
class Subclass(Base):
    __slots__ = "d"
```