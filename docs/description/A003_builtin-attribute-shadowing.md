# builtin-attribute-shadowing (A003)
Derived from the flake8-builtins linter.
## What it does
Checks for class attributes and methods that use the same names as
Python builtins.
## Why is this bad?
Reusing a builtin name for the name of an attribute increases the
difficulty of reading and maintaining the code, and can cause
non-obvious errors, as readers may mistake the attribute for the
builtin and vice versa.
Since methods and class attributes typically cannot be referenced directly
from outside the class scope, this rule only applies to those methods
and attributes that both shadow a builtin and are referenced from within
the class scope, as in the following example, where the list[int] return
type annotation resolves to the list method, rather than the builtin:
class Class:
    @staticmethod
    def list() -> None:
        pass
    @staticmethod
    def repeat(value: int, times: int) -> list[int]:
        return [value] * times
Builtins can be marked as exceptions to this rule via the
lint.flake8-builtins.ignorelist configuration option, or
converted to the appropriate dunder method. Methods decorated with
@typing.override or @typing_extensions.override are also
ignored.
## Example
```
class Class:
    @staticmethod
    def list() -> None:
        pass
    @staticmethod
    def repeat(value: int, times: int) -> list[int]:
        return [value] * times
```