# bad-file-permissions (S103)
Added in v0.0.211 ·
Related issues ·
View source
Derived from the flake8-bandit linter.
## What it does
Checks for files with overly permissive permissions.
## Why is this bad?
Overly permissive file permissions may allow unintended access and
arbitrary code execution.
## Example
```
import os
os.chmod("/etc/secrets.txt", 0o666)  # rw-rw-rw-
```
## Use instead:
```
import os
os.chmod("/etc/secrets.txt", 0o600)  # rw-------
Preview
When preview is enabled, the set of bits treated as dangerous matches
upstream Bandit (0o33): S_IWOTH, S_IXOTH, S_IWGRP, and S_IXGRP.
Outside preview, only S_IWOTH and S_IXGRP are flagged.
```