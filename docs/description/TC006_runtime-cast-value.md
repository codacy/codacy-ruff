# runtime-cast-value (TC006)
Derived from the flake8-type-checking linter.
Fix is always available.
## What it does
Checks for unquoted type expressions in typing.cast() calls.
## Why is this bad?
This rule helps enforce a consistent style across your codebase.
It's often necessary to quote the first argument passed to cast(),
as type expressions can involve forward references, or references
to symbols which are only imported in typing.TYPE_CHECKING blocks.
This can lead to a visual inconsistency across different cast() calls,
where some type expressions are quoted but others are not. By enabling
this rule, you ensure that all type expressions passed to cast() are
quoted, enforcing stylistic consistency across all of your cast() calls.
In some cases where cast() is used in a hot loop, this rule may also
help avoid overhead from repeatedly evaluating complex type expressions at
runtime.
## Example
```
from typing import cast
x = cast(dict[str, int], foo)
```
## Use instead:
```
from typing import cast
x = cast("dict[str, int]", foo)
Fix safety
This fix is safe as long as the type expression doesn't span multiple
lines and includes comments on any of the lines apart from the last one.
```