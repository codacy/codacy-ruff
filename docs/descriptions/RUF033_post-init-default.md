# post-init-default (RUF033)
Fix is sometimes available.
## What it does
Checks for __post_init__ dataclass methods with parameter defaults.
## Why is this bad?
Adding a default value to a parameter in a __post_init__ method has no
impact on whether the parameter will have a default value in the dataclass's
generated __init__ method. To create an init-only dataclass parameter with
a default value, you should use an InitVar field in the dataclass's class
body and give that InitVar field a default value.
As the documentation states:
Init-only fields are added as parameters to the generated __init__()
method, and are passed to the optional __post_init__() method. They are
not otherwise used by dataclasses.
## Example
```
from dataclasses import InitVar, dataclass
@dataclass
class Foo:
    bar: InitVar[int] = 0
    def __post_init__(self, bar: int = 1, baz: int = 2) -> None:
        print(bar, baz)
foo = Foo()  # Prints '0 2'.
```
## Use instead:
```
from dataclasses import InitVar, dataclass
@dataclass
class Foo:
    bar: InitVar[int] = 1
    baz: InitVar[int] = 2
    def __post_init__(self, bar: int, baz: int) -> None:
        print(bar, baz)
foo = Foo()  # Prints '1 2'.
```