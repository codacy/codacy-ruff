# suspicious-ftplib-import (S402)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the ftplib module.
## Why is this bad?
FTP is considered insecure. Instead, use SSH, SFTP, SCP, or another
encrypted protocol.
## Example
```
import ftplib
```