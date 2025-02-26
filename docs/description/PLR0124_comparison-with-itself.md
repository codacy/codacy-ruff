# comparison-with-itself (PLR0124)
Derived from the Pylint linter.
## What it does
Checks for operations that compare a name to itself.
## Why is this bad?
Comparing a name to itself always results in the same value, and is likely
a mistake.
## Example
```
foo == foo
In some cases, self-comparisons are used to determine whether a float is
NaN. Instead, prefer math.isnan:
import math
math.isnan(foo)
```