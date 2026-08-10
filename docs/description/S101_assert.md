# assert (S101)
Added in v0.0.116 ·
Related issues ·
View source
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the assert keyword.
## Why is this bad?
Assertions are removed when Python is run with optimization requested
(i.e., when the -O flag is present), which is a common practice in
production environments. As such, assertions should not be used for runtime
validation of user input or to enforce interface constraints.
Consider raising a meaningful error instead of using assert.
The rule exempts assertions within a TYPE_CHECKING block, assuming these are needed to satisfy
a type checker.
## Example
```
assert x > 0, "Expected positive value."
```
## Use instead:
```
if not x > 0:
    raise ValueError("Expected positive value.")
# or even better:
if x <= 0:
    raise ValueError("Expected positive value.")
```