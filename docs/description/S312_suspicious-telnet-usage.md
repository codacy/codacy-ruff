# suspicious-telnet-usage (S312)
Derived from the flake8-bandit linter.
## What it does
Checks for the use of Telnet-related functions.
## Why is this bad?
Telnet is considered insecure because it does not encrypt data sent over
the connection and is vulnerable to numerous attacks.
Instead, consider using a more secure protocol such as SSH.
In preview, this rule will also flag references to Telnet-related functions.
```