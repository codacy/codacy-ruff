# module-import-not-at-top-of-file (E402)
Derived from the pycodestyle linter.
## What it does
Checks for imports that are not at the top of the file.
## Why is this bad?
According to PEP 8, "imports are always put at the top of the file, just after any
module comments and docstrings, and before module globals and constants."
This rule makes an exception for both sys.path modifications (allowing for
sys.path.insert, sys.path.append, etc.) and os.environ modifications
between imports.
## Example
```
"One string"
"Two string"
a = 1
import os
from sys import x
```
## Use instead:
```
import os
from sys import x
"One string"
"Two string"
a = 1
Notebook behavior
For Jupyter notebooks, this rule checks for imports that are not at the top of a cell.
```