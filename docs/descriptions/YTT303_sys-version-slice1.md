# sys-version-slice1 (YTT303)
Derived from the flake8-2020 linter.
## What it does
Checks for uses of sys.version[:1].
## Why is this bad?
If the major version number consists of more than one digit, this will
select the first digit of the major version number only (e.g., "10.0"
would evaluate to "1"). This is likely unintended, and can lead to subtle
bugs in future versions of Python if the version string is used to test
against a specific major version number.
Instead, use sys.version_info.major to access the current major version
number.
## Example
```
import sys
sys.version[:1]  # If using Python 10, this evaluates to "1".
```
## Use instead:
```
import sys
f"{sys.version_info.major}"  # If using Python 10, this evaluates to "10".
```