# nan-comparison (PLW0177)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for comparisons against NaN values.
## Why is this bad?
Comparing against a NaN value can lead to unexpected results. For example,
float("NaN") == float("NaN") will return False and, in general,
x == float("NaN") will always return False, even if x is NaN.
To determine whether a value is NaN, use math.isnan or np.isnan
instead of comparing against NaN directly.
## Example
```
if x == float("NaN"):
    pass
```
## Use instead:
```
import math
if math.isnan(x):
    pass
```