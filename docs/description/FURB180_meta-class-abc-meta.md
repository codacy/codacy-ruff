# meta-class-abc-meta (FURB180)
Preview (since v0.2.0) ·
Related issues ·
View source
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
import abc
class C(metaclass=abc.ABCMeta):
    pass
```
## Use instead:
```
import abc
class C(abc.ABC):
    pass
Fix safety
The rule's fix is unsafe if the class has base classes. This is because the base classes might
be validating the class's other base classes (e.g., typing.Protocol does this) or otherwise
alter runtime behavior if more base classes are added.
The rule's fix will also be marked as unsafe if the class has
comments in its argument list that could be deleted.
```