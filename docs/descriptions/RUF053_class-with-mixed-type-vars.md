# class-with-mixed-type-vars (RUF053)
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for classes that have PEP 695
while also inheriting from typing.Generic or typing_extensions.Generic.
## Why is this bad?
Such classes cause errors at runtime:
from typing import Generic, TypeVar
U = TypeVar("U")
# TypeError: Cannot inherit from Generic[...] multiple times.
class C[T](Generic[U]): ...
## Example
```
from typing import Generic, ParamSpec, TypeVar, TypeVarTuple
U = TypeVar("U")
P = ParamSpec("P")
Ts = TypeVarTuple("Ts")
class C[T](Generic[U, P, *Ts]): ...
```
## Use instead:
```
class C[T, U, **P, *Ts]: ...
Fix safety
As the fix changes runtime behaviour, it is always marked as unsafe.
Additionally, comments within the fix range will not be preserved.
```