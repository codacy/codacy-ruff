# unused-private-protocol (PYI046)
Derived from the flake8-pyi linter.
## What it does
Checks for the presence of unused private typing.Protocol definitions.
## Why is this bad?
A private typing.Protocol that is defined but not used is likely a
mistake. It should either be used, made public, or removed to avoid
confusion.
## Example
```
import typing
class _PrivateProtocol(typing.Protocol):
    foo: int
```
## Use instead:
```
import typing
class _PrivateProtocol(typing.Protocol):
    foo: int
def func(arg: _PrivateProtocol) -> None: ...
```