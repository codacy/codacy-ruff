# shallow-copy-environ (PLW1507)
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Check for shallow os.environ copies.
## Why is this bad?
os.environ is not a dict object, but rather, a proxy object. As such, mutating a shallow
copy of os.environ will also mutate the original object.
See: #15373 for more information.
## Example
```
import copy
import os
env = copy.copy(os.environ)
```
## Use instead:
```
import os
env = os.environ.copy()
```