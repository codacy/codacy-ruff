# sys-version-slice3 (YTT101)
Derived from the flake8-2020 linter.
## What it does
Checks for uses of sys.version[:3].
## Why is this bad?
If the current major or minor version consists of multiple digits,
sys.version[:3] will truncate the version number (e.g., "3.10" would
become "3.1"). This is likely unintended, and can lead to subtle bugs if
the version string is used to test against a specific Python version.
Instead, use sys.version_info to access the current major and minor
version numbers as a tuple, which can be compared to other tuples
without issue.
## Example
```
import sys
sys.version[:3]  # Evaluates to "3.1" on Python 3.10.
```
## Use instead:
```
import sys
sys.version_info[:2]  # Evaluates to (3, 10) on Python 3.10.
```