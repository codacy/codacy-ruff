# complex-if-statement-in-stub (PYI002)
Derived from the flake8-pyi linter.
## What it does
Checks for if statements with complex conditionals in stubs.
## Why is this bad?
Type checkers understand simple conditionals to express variations between
different Python versions and platforms. However, complex tests may not be
understood by a type checker, leading to incorrect inferences when they
analyze your code.
## Example
```
import sys
if (3, 10) <= sys.version_info < (3, 12): ...
```
## Use instead:
```
import sys
if sys.version_info >= (3, 10) and sys.version_info < (3, 12): ...
```