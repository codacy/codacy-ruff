# numpy-legacy-random (NPY002)
## What it does
Checks for the use of legacy np.random function calls.
## Why is this bad?
According to the NumPy documentation's Legacy Random Generation:
The RandomState provides access to legacy generators... This class
should only be used if it is essential to have randoms that are
identical to what would have been produced by previous versions of
NumPy.
The members exposed directly on the random module are convenience
functions that alias to methods on a global singleton RandomState
instance. NumPy recommends using a dedicated Generator instance
rather than the random variate generation methods exposed directly on
the random module, as the new Generator is both faster and has
better statistical properties.
See the documentation on Random Sampling and NEP 19 for further
details.
## Examples
```
import numpy as np
np.random.seed(1337)
np.random.normal()
```
## Use instead:
```
rng = np.random.default_rng(1337)
rng.normal()
```