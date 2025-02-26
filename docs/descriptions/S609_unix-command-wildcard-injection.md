# unix-command-wildcard-injection (S609)
Derived from the flake8-bandit linter.
## What it does
Checks for possible wildcard injections in calls to subprocess.Popen().
## Why is this bad?
Wildcard injections can lead to unexpected behavior if unintended files are
matched by the wildcard. Consider using a more specific path instead.
## Example
```
import subprocess
subprocess.Popen(["chmod", "777", "*.py"])
```
## Use instead:
```
import subprocess
subprocess.Popen(["chmod", "777", "main.py"])
```