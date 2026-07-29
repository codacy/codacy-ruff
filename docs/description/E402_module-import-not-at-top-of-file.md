# module-import-not-at-top-of-file (E402)
Added in v0.0.28 ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is sometimes available.
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
Fix safety
This rule's fix is marked as unsafe as imports moved to the top of the file
are placed above existing imports, in reverse order than they were in the
file. Re-ordering imports is unsafe as it can change the execution order of
the imported code.
```