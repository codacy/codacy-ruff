# redefined-while-unused (F811)
Added in v0.0.171 ·
Related issues ·
View source
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for variable definitions that redefine (or "shadow") unused
variables.
## Why is this bad?
Redefinitions of unused names are unnecessary and often indicative of a
mistake.
## Example
```
import foo
import bar
import foo  # Redefinition of unused `foo` from line 1
```
## Use instead:
```
import foo
import bar
Preview
When preview is enabled, this rule also flags annotated variable
redeclarations. For example, bar: int = 1 followed by bar: int = 2
will be flagged as a redefinition of an unused variable, whereas plain
reassignments like bar = 1 followed by bar = 2 remain unflagged.
In preview, this rule will also flag redefinitions in typing.TYPE_CHECKING blocks:
import typing
from collections.abc import Sequence
if typing.TYPE_CHECKING:
    # Redefinition of unused `Sequence` from line 2
    from collections.abc import Sequence
```
## Use instead:
```
from collections.abc import Sequence
```