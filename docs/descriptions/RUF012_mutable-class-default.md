# mutable-class-default (RUF012)
## What it does
Checks for mutable default values in class attributes.
## Why is this bad?
Mutable default values share state across all instances of the class,
while not being obvious. This can lead to bugs when the attributes are
changed in one instance, as those changes will unexpectedly affect all
other instances.
Generally speaking, you probably want to avoid having mutable default
values in the class body at all; instead, these variables should usually
be initialized in __init__. However, other possible fixes for the issue
can include:
Explicitly annotating the variable with typing.ClassVar to
    indicate that it is intended to be shared across all instances.
Using an immutable data type (e.g. a tuple instead of a list)
    for the default value.
## Example
```
class A:
    variable_1: list[int] = []
    variable_2: set[int] = set()
    variable_3: dict[str, int] = {}
```
## Use instead:
```
class A:
    def __init__(self) -> None:
        self.variable_1: list[int] = []
        self.variable_2: set[int] = set()
        self.variable_3: dict[str, int] = {}
Or:
from typing import ClassVar
class A:
    variable_1: ClassVar[list[int]] = []
    variable_2: ClassVar[set[int]] = set()
    variable_3: ClassVar[dict[str, int]] = {}
Or:
class A:
    variable_1: list[int] | None = None
    variable_2: set[int] | None = None
    variable_3: dict[str, int] | None = None
Or:
from collections.abc import Sequence, Mapping, Set as AbstractSet
from types import MappingProxyType
class A:
    variable_1: Sequence[int] = ()
    variable_2: AbstractSet[int] = frozenset()
    variable_3: Mapping[str, int] = MappingProxyType({})
```