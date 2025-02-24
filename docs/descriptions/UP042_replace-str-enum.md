# replace-str-enum (UP042)
Derived from the pyupgrade linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for classes that inherit from both str and enum.Enum.
## Why is this bad?
Python 3.11 introduced enum.StrEnum, which is preferred over inheriting
from both str and enum.Enum.
## Example
```
import enum
class Foo(str, enum.Enum): ...
```
## Use instead:
```
import enum
class Foo(enum.StrEnum): ...
Fix safety
Python 3.11 introduced a breaking change for enums that inherit from both
str and enum.Enum. Consider the following enum:
from enum import Enum
class Foo(str, Enum):
    BAR = "bar"
In Python 3.11, the formatted representation of Foo.BAR changed as
follows:
# Python 3.10
f"{Foo.BAR}"  # > bar
# Python 3.11
f"{Foo.BAR}"  # > Foo.BAR
Migrating from str and enum.Enum to enum.StrEnum will restore the
previous behavior, such that:
from enum import StrEnum
class Foo(StrEnum):
    BAR = "bar"
f"{Foo.BAR}"  # > bar
As such, migrating to enum.StrEnum will introduce a behavior change for
code that relies on the Python 3.11 behavior.
```