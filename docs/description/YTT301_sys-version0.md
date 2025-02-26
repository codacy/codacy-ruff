# sys-version0 (YTT301)
Derived from the flake8-2020 linter.
## What it does
Checks for uses of sys.version[0].
## Why is this bad?
If the current major or minor version consists of multiple digits,
sys.version[0] will select the first digit of the major version number
only (e.g., "10.2" would evaluate to "1"). This is likely unintended,
and can lead to subtle bugs if the version string is used to test against a
major version number.
Instead, use sys.version_info.major to access the current major version
number.
## Example
```
import sys
sys.version[0]  # If using Python 10, this evaluates to "1".
```
## Use instead:
```
import sys
f"{sys.version_info.major}"  # If using Python 10, this evaluates to "10".
```