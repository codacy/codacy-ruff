# shallow-copy-environ (PLW1507)
Derived from the Pylint linter.
Fix is always available.
## What it does
Check for shallow os.environ copies.
## Why is this bad?
os.environ is not a dict object, but rather, a proxy object. As such, mutating a shallow
copy of os.environ will also mutate the original object.
See BPO 15373 for more information.
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
Fix safety
This rule's fix is marked as unsafe because replacing a shallow copy with a deep copy can lead
to unintended side effects. If the program modifies the shallow copy at some point, changing it
to a deep copy may prevent those modifications from affecting the original data, potentially
altering the program's behavior.
```