# start-process-with-a-shell (S605)
Derived from the flake8-bandit linter.
## What it does
Checks for calls that start a process with a shell, providing guidance on
whether the usage is safe or not.
## Why is this bad?
Starting a process with a shell can introduce security risks, such as
code injection vulnerabilities. It's important to be aware of whether the
usage of the shell is safe or not.
This rule triggers on functions like os.system, popen, etc., which
start processes with a shell. It evaluates whether the provided command
is a literal string or an expression. If the command is a literal string,
it's considered safe. If the command is an expression, it's considered
(potentially) unsafe.
## Example
```
import os
# Safe usage (literal string)
command = "ls -l"
os.system(command)
# Potentially unsafe usage (expression)
cmd = get_user_input()
os.system(cmd)
Note
The subprocess module provides more powerful facilities for spawning new
processes and retrieving their results, and using that module is preferable
to using os.system or similar functions. Consider replacing such usages
with subprocess.call or related functions.
```