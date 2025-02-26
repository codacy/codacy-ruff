# subprocess-run-without-check (PLW1510)
Derived from the Pylint linter.
Fix is always available.
## What it does
Checks for uses of subprocess.run without an explicit check argument.
## Why is this bad?
By default, subprocess.run does not check the return code of the process
it runs. This can lead to silent failures.
Instead, consider using check=True to raise an exception if the process
fails, or set check=False explicitly to mark the behavior as intentional.
## Example
```
import subprocess
subprocess.run(["ls", "nonexistent"])  # No exception raised.
```
## Use instead:
```
import subprocess
subprocess.run(["ls", "nonexistent"], check=True)  # Raises exception.
Or:
import subprocess
subprocess.run(["ls", "nonexistent"], check=False)  # Explicitly no check.
Fix safety
This rule's fix is marked as unsafe for function calls that contain
**kwargs, as adding a check keyword argument to such a call may lead
to a duplicate keyword argument error.
```