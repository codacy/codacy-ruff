# bad-exit-annotation (PYI036)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for incorrect function signatures on __exit__ and __aexit__
methods.
## Why is this bad?
Improperly annotated __exit__ and __aexit__ methods can cause
unexpected behavior when interacting with type checkers.
## Example
```
from types import TracebackType
class Foo:
    def __exit__(
        self, typ: BaseException, exc: BaseException, tb: TracebackType
    ) -> None: ...
```
## Use instead:
```
from types import TracebackType
class Foo:
    def __exit__(
        self,
        typ: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None: ...
```