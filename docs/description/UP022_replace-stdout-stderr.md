# replace-stdout-stderr (UP022)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for uses of subprocess.run that send stdout and stderr to a
pipe.
## Why is this bad?
As of Python 3.7, subprocess.run has a capture_output keyword argument
that can be set to True to capture stdout and stderr outputs. This is
equivalent to setting stdout and stderr to subprocess.PIPE, but is
more explicit and readable.
## Example
```
import subprocess
subprocess.run(["foo"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
```
## Use instead:
```
import subprocess
subprocess.run(["foo"], capture_output=True)
```