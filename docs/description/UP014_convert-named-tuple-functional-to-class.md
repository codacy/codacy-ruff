# convert-named-tuple-functional-to-class (UP014)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for NamedTuple declarations that use functional syntax.
## Why is this bad?
NamedTuple subclasses can be defined either through a functional syntax
(Foo = NamedTuple(...)) or a class syntax (class Foo(NamedTuple): ...).
The class syntax is more readable and generally preferred over the
functional syntax, which exists primarily for backwards compatibility
with collections.namedtuple.
## Example
```
from typing import NamedTuple
Foo = NamedTuple("Foo", [("a", int), ("b", str)])
```
## Use instead:
```
from typing import NamedTuple
class Foo(NamedTuple):
    a: int
    b: str
Fix safety
This rule's fix is marked as unsafe if there are any comments within the
range of the NamedTuple definition, as these will be dropped by the
autofix.
```