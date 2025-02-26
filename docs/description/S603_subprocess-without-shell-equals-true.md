# subprocess-without-shell-equals-true (S603)
Derived from the flake8-bandit linter.
## What it does
Check for method calls that initiate a subprocess without a shell.
## Why is this bad?
Starting a subprocess without a shell can prevent attackers from executing
arbitrary shell commands; however, it is still error-prone. Consider
validating the input.
Known problems
Prone to false positives as it is difficult to determine whether the
passed arguments have been validated (#4045).
## Example
```
import subprocess
cmd = input("Enter a command: ").split()
subprocess.run(cmd)
```