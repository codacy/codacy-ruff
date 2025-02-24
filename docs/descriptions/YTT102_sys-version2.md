# sys-version2 (YTT102)
Derived from the flake8-2020 linter.
## What it does
Checks for uses of sys.version[2].
## Why is this bad?
If the current major or minor version consists of multiple digits,
sys.version[2] will select the first digit of the minor number only
(e.g., "3.10" would evaluate to "1"). This is likely unintended, and
can lead to subtle bugs if the version is used to test against a minor
version number.
Instead, use sys.version_info.minor to access the current minor version
number.
## Example
```
import sys
sys.version[2]  # Evaluates to "1" on Python 3.10.
```
## Use instead:
```
import sys
f"{sys.version_info.minor}"  # Evaluates to "10" on Python 3.10.
```