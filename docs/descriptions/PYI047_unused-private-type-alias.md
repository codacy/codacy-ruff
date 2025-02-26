# unused-private-type-alias (PYI047)
Derived from the flake8-pyi linter.
## What it does
Checks for the presence of unused private type aliases.
## Why is this bad?
A private type alias that is defined but not used is likely a
mistake. It should either be used, made public, or removed to avoid
confusion.
## Example
```
import typing
_UnusedTypeAlias: typing.TypeAlias = int
```
## Use instead:
```
import typing
_UsedTypeAlias: typing.TypeAlias = int
def func(arg: _UsedTypeAlias) -> _UsedTypeAlias: ...
```