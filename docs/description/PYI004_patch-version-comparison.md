# patch-version-comparison (PYI004)
Derived from the flake8-pyi linter.
## What it does
Checks for Python version comparisons in stubs that compare against patch
versions (e.g., Python 3.8.3) instead of major and minor versions (e.g.,
Python 3.8).
## Why is this bad?
Stub files support simple conditionals to test for differences in Python
versions and platforms. However, type checkers only understand a limited
subset of these conditionals. In particular, type checkers don't support
patch versions (e.g., Python 3.8.3), only major and minor versions (e.g.,
Python 3.8). Therefore, version checks in stubs should only use the major
and minor versions.
## Example
```
import sys
if sys.version_info >= (3, 4, 3): ...
```
## Use instead:
```
import sys
if sys.version_info >= (3, 4): ...
```