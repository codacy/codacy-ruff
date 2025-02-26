# bad-version-info-order (PYI066)
Derived from the flake8-pyi linter.
## What it does
Checks for code that branches on sys.version_info comparisons where
branches corresponding to older Python versions come before branches
corresponding to newer Python versions.
## Why is this bad?
As a convention, branches that correspond to newer Python versions should
come first. This makes it easier to understand the desired behavior, which
typically corresponds to the latest Python versions.
This rule enforces the convention by checking for if tests that compare
sys.version_info with < rather than >=.
By default, this rule only applies to stub files.
In preview, it will also flag this anti-pattern in non-stub files.
## Example
```
import sys
if sys.version_info < (3, 10):
    def read_data(x, *, preserve_order=True): ...
else:
    def read_data(x): ...
```
## Use instead:
```
if sys.version_info >= (3, 10):
    def read_data(x): ...
else:
    def read_data(x, *, preserve_order=True): ...
```