# suspicious-pyghmi-import (S415)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the pyghmi module.
## Why is this bad?
pyghmi is an IPMI-related module, but IPMI is considered insecure.
Instead, use an encrypted protocol.
## Example
```
import pyghmi
```