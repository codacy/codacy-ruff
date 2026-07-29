# uncapitalized-environment-variables (SIM112)
Added in v0.0.218 ·
Related issues ·
View source
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Check for environment variables that are not capitalized.
## Why is this bad?
By convention, environment variables should be capitalized.
Furthermore, os.environ behaves differently across platforms. On Windows,
os.environ automatically converts environment variable names to uppercase.
This means that if you define a lowercase environment variable (e.g., foo=1),
iterating over os.environ will yield FOO on Windows, but
foo on Linux and macOS. This can lead to subtle bugs in cross-platform code
if it assumes environment variables preserve their original case.
## Example
```
import os
os.environ["foo"]
```
## Use instead:
```
import os
os.environ["FOO"]
Fix safety
This fix is always marked as unsafe because automatically capitalizing environment variable names
can change program behavior in environments where the variable names are case-sensitive, such as most
Unix-like systems.
```