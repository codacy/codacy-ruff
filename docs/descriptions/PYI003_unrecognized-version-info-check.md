# unrecognized-version-info-check (PYI003)
Derived from the flake8-pyi linter.
## What it does
Checks for problematic sys.version_info-related conditions in stubs.
## Why is this bad?
Stub files support simple conditionals to test for differences in Python
versions using sys.version_info. However, there are a number of common
mistakes involving sys.version_info comparisons that should be avoided.
For example, comparing against a string can lead to unexpected behavior.
## Example
```
import sys
if sys.version_info[0] == "2": ...
```
## Use instead:
```
import sys
if sys.version_info[0] == 2: ...
```