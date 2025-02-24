# unquoted-type-alias (TC007)
Derived from the flake8-type-checking linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks if PEP 613 explicit type aliases contain references to
symbols that are not available at runtime.
## Why is this bad?
Referencing type-checking only symbols results in a NameError at runtime.
## Example
```
from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    from foo import Foo
OptFoo: TypeAlias = Foo | None
```
## Use instead:
```
from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    from foo import Foo
OptFoo: TypeAlias = "Foo | None"
Fix safety
This rule's fix is currently always marked as unsafe, since runtime
typing libraries may try to access/resolve the type alias in a way
that we can't statically determine during analysis and relies on the
type alias not containing any forward references.
```