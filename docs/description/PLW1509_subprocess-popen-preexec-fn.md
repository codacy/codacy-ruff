# subprocess-popen-preexec-fn (PLW1509)
Derived from the Pylint linter.
## What it does
Checks for uses of subprocess.Popen with a preexec_fn argument.
## Why is this bad?
The preexec_fn argument is unsafe within threads as it can lead to
deadlocks. Furthermore, preexec_fn is targeted for deprecation.
Instead, consider using task-specific arguments such as env,
start_new_session, and process_group. These are not prone to deadlocks
and are more explicit.
## Example
```
import os, subprocess
subprocess.Popen(foo, preexec_fn=os.setsid)
subprocess.Popen(bar, preexec_fn=os.setpgid(0, 0))
```
## Use instead:
```
import subprocess
subprocess.Popen(foo, start_new_session=True)
subprocess.Popen(bar, process_group=0)  # Introduced in Python 3.11
```