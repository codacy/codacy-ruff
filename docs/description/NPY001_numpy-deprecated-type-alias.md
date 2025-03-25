# numpy-deprecated-type-alias (NPY001)
Fix is sometimes available.
## What it does
Checks for deprecated NumPy type aliases.
## Why is this bad?
NumPy's np.int has long been an alias of the builtin int; the same
is true of np.float and others. These aliases exist primarily
for historic reasons, and have been a cause of frequent confusion
for newcomers.
These aliases were deprecated in 1.20, and removed in 1.24.
Note, however, that np.bool and np.long were reintroduced in 2.0 with
different semantics, and are thus omitted from this rule.
## Example
```
import numpy as np
np.int
```
## Use instead:
```
int
```