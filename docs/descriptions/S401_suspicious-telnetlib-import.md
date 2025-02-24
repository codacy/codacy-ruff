# suspicious-telnetlib-import (S401)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the telnetlib module.
## Why is this bad?
Telnet is considered insecure. It is deprecated since version 3.11, and
was removed in version 3.13. Instead, use SSH or another encrypted
protocol.
## Example
```
import telnetlib
```