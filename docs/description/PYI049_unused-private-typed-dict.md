# unused-private-typed-dict (PYI049)
Derived from the flake8-pyi linter.
## What it does
Checks for the presence of unused private typing.TypedDict definitions.
## Why is this bad?
A private typing.TypedDict that is defined but not used is likely a
mistake. It should either be used, made public, or removed to avoid
confusion.
## Example
```
import typing
class _UnusedPrivateTypedDict(typing.TypedDict):
    foo: list[int]
```
## Use instead:
```
import typing
class _UsedPrivateTypedDict(typing.TypedDict):
    foo: set[str]
def func(arg: _UsedPrivateTypedDict) -> _UsedPrivateTypedDict: ...
```