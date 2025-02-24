# redundant-none-literal (PYI061)
Derived from the flake8-pyi linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for redundant Literal[None] annotations.
## Why is this bad?
While Literal[None] is a valid type annotation, it is semantically equivalent to None.
Prefer None over Literal[None] for both consistency and readability.
## Example
```
from typing import Literal
Literal[None]
Literal[1, 2, 3, "foo", 5, None]
```
## Use instead:
```
from typing import Literal
None
Literal[1, 2, 3, "foo", 5] | None
Fix safety and availability
This rule's fix is marked as safe unless the literal contains comments.
There is currently no fix available when applying the fix would lead to
a TypeError from an expression of the form None | None or when we
are unable to import the symbol typing.Optional and the Python version
is 3.9 or below.
```