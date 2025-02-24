# meta-class-abc-meta (FURB180)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of metaclass=abc.ABCMeta to define abstract base classes
(ABCs).
## Why is this bad?
Instead of class C(metaclass=abc.ABCMeta): ..., use class C(ABC): ...
to define an abstract base class. Inheriting from the ABC wrapper class
is semantically identical to setting metaclass=abc.ABCMeta, but more
succinct.
## Example
```
class C(metaclass=ABCMeta):
    pass
```
## Use instead:
```
class C(ABC):
    pass
```