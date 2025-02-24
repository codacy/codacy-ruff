# suspicious-subprocess-import (S404)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the subprocess module.
## Why is this bad?
It is possible to inject malicious commands into subprocess calls. Consider
possible security implications associated with this module.
## Example
```
import subprocess
```