# subprocess-popen-with-shell-equals-true (S602)
Derived from the flake8-bandit linter.
## What it does
Check for method calls that initiate a subprocess with a shell.
## Why is this bad?
Starting a subprocess with a shell can allow attackers to execute arbitrary
shell commands. Consider starting the process without a shell call and
sanitize the input to mitigate the risk of shell injection.
## Example
```
import subprocess
subprocess.run("ls -l", shell=True)
```
## Use instead:
```
import subprocess
subprocess.run(["ls", "-l"])
```