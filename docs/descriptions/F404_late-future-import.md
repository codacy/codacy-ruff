# late-future-import (F404)
Derived from the Pyflakes linter.
## What it does
Checks for __future__ imports that are not located at the beginning of a
file.
## Why is this bad?
Imports from __future__ must be placed the beginning of the file, before any
other statements (apart from docstrings). The use of __future__ imports
elsewhere is invalid and will result in a SyntaxError.
## Example
```
from pathlib import Path
from __future__ import annotations
```
## Use instead:
```
from __future__ import annotations
from pathlib import Path
```