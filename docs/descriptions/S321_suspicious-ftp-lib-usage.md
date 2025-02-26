# suspicious-ftp-lib-usage (S321)
Derived from the flake8-bandit linter.
## What it does
Checks for the use of FTP-related functions.
## Why is this bad?
FTP is considered insecure as it does not encrypt data sent over the
connection and is thus vulnerable to numerous attacks.
Instead, consider using FTPS (which secures FTP using SSL/TLS) or SFTP.
In preview, this rule will also flag references to FTP-related functions.
```