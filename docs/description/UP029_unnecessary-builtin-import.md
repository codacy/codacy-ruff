# unnecessary-builtin-import (UP029)
Added in v0.0.211 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for imports of Python 3 builtins from Python 2 compatibility shims
such as python-future and six.
## Why is this bad?
These shims existed to access Python 3 builtins from code that also ran on
Python 2. On Python 3-only code, the imports are redundant.
## Example
```
from builtins import str
str(1)
```
## Use instead:
```
str(1)
Fix safety
This fix is marked as unsafe because it will remove comments attached to the unused import.
```