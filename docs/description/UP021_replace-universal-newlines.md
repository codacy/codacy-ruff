# replace-universal-newlines (UP021)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of subprocess.run that set the universal_newlines
keyword argument.
## Why is this bad?
As of Python 3.7, the universal_newlines keyword argument has been
renamed to text, and now exists for backwards compatibility. The
universal_newlines keyword argument may be removed in a future version of
Python. Prefer text, which is more explicit and readable.
## Example
```
import subprocess
subprocess.run(["foo"], universal_newlines=True)
```
## Use instead:
```
import subprocess
subprocess.run(["foo"], text=True)
```