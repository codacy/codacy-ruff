# unused-private-type-var (PYI018)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for the presence of unused private TypeVar, ParamSpec or
TypeVarTuple declarations.
## Why is this bad?
A private TypeVar that is defined but not used is likely a mistake. It
should either be used, made public, or removed to avoid confusion. A type
variable is considered "private" if its name starts with an underscore.
## Example
```
import typing
import typing_extensions
_T = typing.TypeVar("_T")
_Ts = typing_extensions.TypeVarTuple("_Ts")
Fix safety and availability
This rule's fix is available when preview mode is enabled.
It is always marked as unsafe, as it would break your code if the type
variable is imported by another module.
```