# wrong-tuple-length-version-comparison (PYI005)
Derived from the flake8-pyi linter.
## What it does
Checks for Python version comparisons that compare against a tuple of the
wrong length.
## Why is this bad?
Stub files support simple conditionals to test for differences in Python
versions and platforms. When comparing against sys.version_info, avoid
comparing against tuples of the wrong length, which can lead to unexpected
behavior.
## Example
```
import sys
if sys.version_info[:2] == (3,): ...
```
## Use instead:
```
import sys
if sys.version_info[0] == 3: ...
```