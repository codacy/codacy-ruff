# sys-version-cmp-str3 (YTT103)
Derived from the flake8-2020 linter.
## What it does
Checks for comparisons that test sys.version against string literals,
such that the comparison will evaluate to False on Python 3.10 or later.
## Why is this bad?
Comparing sys.version to a string is error-prone and may cause subtle
bugs, as the comparison will be performed lexicographically, not
semantically. For example, sys.version > "3.9" will evaluate to False
when using Python 3.10, as "3.10" is lexicographically "less" than
"3.9".
Instead, use sys.version_info to access the current major and minor
version numbers as a tuple, which can be compared to other tuples
without issue.
## Example
```
import sys
sys.version > "3.9"  # `False` on Python 3.10.
```
## Use instead:
```
import sys
sys.version_info > (3, 9)  # `True` on Python 3.10.
```