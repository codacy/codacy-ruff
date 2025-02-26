# never-union (RUF020)
Fix is sometimes available.
## What it does
Checks for uses of typing.NoReturn and typing.Never in union types.
## Why is this bad?
typing.NoReturn and typing.Never are special types, used to indicate
that a function never returns, or that a type has no values.
Including typing.NoReturn or typing.Never in a union type is redundant,
as, e.g., typing.Never | T is equivalent to T.
## Example
```
from typing import Never
def func() -> Never | int: ...
```
## Use instead:
```
def func() -> int: ...
```