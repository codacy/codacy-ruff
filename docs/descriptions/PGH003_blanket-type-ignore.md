# blanket-type-ignore (PGH003)
Derived from the pygrep-hooks linter.
## What it does
Check for type: ignore annotations that suppress all type warnings, as
opposed to targeting specific type warnings.
## Why is this bad?
Suppressing all warnings can hide issues in the code.
Blanket type: ignore annotations are also more difficult to interpret and
maintain, as the annotation does not clarify which warnings are intended
to be suppressed.
## Example
```
from foo import secrets  # type: ignore
```
## Use instead:
```
from foo import secrets  # type: ignore[attr-defined]
```