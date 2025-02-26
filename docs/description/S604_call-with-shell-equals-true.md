# call-with-shell-equals-true (S604)
Derived from the flake8-bandit linter.
## What it does
Checks for method calls that set the shell parameter to true or another
truthy value when invoking a subprocess.
## Why is this bad?
Setting the shell parameter to true or another truthy value when
invoking a subprocess can introduce security vulnerabilities, as it allows
shell metacharacters and whitespace to be passed to child processes,
potentially leading to shell injection attacks.
It is recommended to avoid using shell=True unless absolutely necessary
and, when used, to ensure that all inputs are properly sanitized and quoted
to prevent such vulnerabilities.
Known problems
Prone to false positives as it is triggered on any function call with a
shell=True parameter.
## Example
```
import subprocess
user_input = input("Enter a command: ")
subprocess.run(user_input, shell=True)
```