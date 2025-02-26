# type-bivariance (PLC0131)
Derived from the Pylint linter.
## What it does
Checks for TypeVar and ParamSpec definitions in which the type is
both covariant and contravariant.
## Why is this bad?
By default, Python's generic types are invariant, but can be marked as
either covariant or contravariant via the covariant and contravariant
keyword arguments. While the API does allow you to mark a type as both
covariant and contravariant, this is not supported by the type system,
and should be avoided.
Instead, change the variance of the type to be either covariant,
contravariant, or invariant. If you want to describe both covariance and
contravariance, consider using two separate type parameters.
For context: an "invariant" generic type only accepts values that exactly
match the type parameter; for example, list[Dog] accepts only list[Dog],
not list[Animal] (superclass) or list[Bulldog] (subclass). This is
the default behavior for Python's generic types.
A "covariant" generic type accepts subclasses of the type parameter; for
example, Sequence[Animal] accepts Sequence[Dog]. A "contravariant"
generic type accepts superclasses of the type parameter; for example,
Callable[Dog] accepts Callable[Animal].
## Example
```
from typing import TypeVar
T = TypeVar("T", covariant=True, contravariant=True)
```
## Use instead:
```
from typing import TypeVar
T_co = TypeVar("T_co", covariant=True)
T_contra = TypeVar("T_contra", contravariant=True)
```