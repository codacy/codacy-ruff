# paramiko-call (S601)
Added in v0.0.270 ·
Related issues ·
View source
Derived from the flake8-bandit linter.
## What it does
Checks for paramiko calls.
## Why is this bad?
paramiko calls allow users to execute arbitrary shell commands on a
remote machine. If the inputs to these calls are not properly sanitized,
they can be vulnerable to shell injection attacks.
## Example
```
import paramiko
client = paramiko.SSHClient()
client.exec_command("echo $HOME")
```