# function-call-in-dataclass-default-argument (RUF009)
## What it does
Checks for function calls in dataclass attribute defaults.
## Why is this bad?
Function calls are only performed once, at definition time. The returned
value is then reused by all instances of the dataclass. This can lead to
unexpected behavior when the function call returns a mutable object, as
changes to the object will be shared across all instances.
If a field needs to be initialized with a mutable object, use the
field(default_factory=...) pattern.
Attributes whose default arguments are NewType calls
where the original type is immutable are ignored.
## Example
```
from dataclasses import dataclass
def simple_list() -> list[int]:
    return [1, 2, 3, 4]
@dataclass
class A:
    mutable_default: list[int] = simple_list()
```
## Use instead:
```
from dataclasses import dataclass, field
def creating_list() -> list[int]:
    return [1, 2, 3, 4]
@dataclass
class A:
    mutable_default: list[int] = field(default_factory=creating_list)
```