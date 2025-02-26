# numpy-deprecated-function (NPY003)
Fix is sometimes available.
## What it does
Checks for uses of deprecated NumPy functions.
## Why is this bad?
When NumPy functions are deprecated, they are usually replaced with
newer, more efficient versions, or with functions that are more
consistent with the rest of the NumPy API.
Prefer newer APIs over deprecated ones.
## Examples
```
import numpy as np
np.alltrue([True, False])
```
## Use instead:
```
import numpy as np
np.all([True, False])
```