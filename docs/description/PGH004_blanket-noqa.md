# blanket-noqa (PGH004)
Derived from the pygrep-hooks linter.
Fix is sometimes available.
## What it does
Check for noqa annotations that suppress all diagnostics, as opposed to
targeting specific diagnostics.
## Why is this bad?
Suppressing all diagnostics can hide issues in the code.
Blanket noqa annotations are also more difficult to interpret and
maintain, as the annotation does not clarify which diagnostics are intended
to be suppressed.
In preview, this rule also checks for blanket file-level annotations (e.g.,
# ruff: noqa, as opposed to # ruff: noqa: F401).
## Example
```
from .base import *  # noqa
```
## Use instead:
```
from .base import *  # noqa: F403
Fix safety
This rule will attempt to fix blanket noqa annotations that appear to
be unintentional. For example, given # noqa F401, the rule will suggest
inserting a colon, as in # noqa: F401.
While modifying noqa comments is generally safe, doing so may introduce
additional diagnostics.
```