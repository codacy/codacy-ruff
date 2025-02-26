# uncapitalized-environment-variables (SIM112)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Check for environment variables that are not capitalized.
## Why is this bad?
By convention, environment variables should be capitalized.
On Windows, environment variables are case-insensitive and are converted to
uppercase, so using lowercase environment variables can lead to subtle bugs.
## Example
```
import os
os.environ["foo"]
```
## Use instead:
```
import os
os.environ["FOO"]
```