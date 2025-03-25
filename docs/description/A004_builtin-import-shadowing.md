# builtin-import-shadowing (A004)
Derived from the flake8-builtins linter.
## What it does
Checks for imports that use the same names as builtins.
## Why is this bad?
Reusing a builtin for the name of an import increases the difficulty
of reading and maintaining the code, and can cause non-obvious errors,
as readers may mistake the variable for the builtin and vice versa.
Builtins can be marked as exceptions to this rule via the
lint.flake8-builtins.ignorelist configuration option.
## Example
```
from rich import print
print("Some message")
```
## Use instead:
```
from rich import print as rich_print
rich_print("Some message")
or:
import rich
rich.print("Some message")
```