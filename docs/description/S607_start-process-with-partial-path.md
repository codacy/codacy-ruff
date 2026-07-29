# start-process-with-partial-path (S607)
Added in v0.0.262 ·
Related issues ·
View source
Derived from the flake8-bandit linter.
## What it does
Checks for the starting of a process with a partial executable path.
## Why is this bad?
Starting a process with a partial executable path can allow attackers to
execute an arbitrary executable by adjusting the PATH environment variable.
Consider using a full path to the executable instead.
## Example
```
import subprocess
subprocess.Popen(["ruff", "check", "file.py"])
```
## Use instead:
```
import subprocess
subprocess.Popen(["/usr/bin/ruff", "check", "file.py"])
```