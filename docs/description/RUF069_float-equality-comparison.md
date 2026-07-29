# float-equality-comparison (RUF069)
Preview (since 0.15.1) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for comparisons between floating-point values using == or !=.
## Why is this bad?
Directly comparing floating-point numbers for exact equality or inequality
can lead to incorrect and non-deterministic outcomes. This is because
floating-point values are finite binary approximations of real numbers.
Many decimal values, such as 0.1, cannot be represented exactly in binary,
leading to small rounding errors. Furthermore, the results of arithmetic
operations are subject to rounding at each step, and the order of operations
can influence the final result. Consequently, two mathematically equivalent
computations may yield binary floating-point values that differ by a tiny
margin. Relying on exact comparison treats these semantically equal values
as different, breaking logical correctness.
How to fix
For general Python code, use tolerance-based comparison functions from the
standard library:
Use math.isclose() for scalar comparisons
Use cmath.isclose() for complex numbers comparisons
Use unittest.assertAlmostEqual() in tests with unittest
Note that math.isclose() and cmath.isclose() have a default absolute tolerance of zero, so
when comparing values near zero, you must explicitly specify an abs_tol
parameter.
Many frameworks and libraries provide their own specialized functions for
floating-point comparison, often with different default tolerances optimized
for their specific use cases:
For NumPy arrays: use numpy.isclose() or numpy.allclose()
For PyTorch tensors: use torch.isclose()
Check your framework's / library's documentation for equivalent functions
For scenarios requiring exact decimal arithmetic, consider using the
Decimal class from the decimal module instead of floating-point numbers.
## Example
```
assert 0.1 + 0.2 == 0.3  # AssertionError
assert complex(0.3, 0.1) == complex(0.1 + 0.2, 0.1)  # AssertionError
```
## Use instead:
```
import cmath
import math
# Scalar comparison
assert math.isclose(0.1 + 0.2, 0.3, abs_tol=1e-9)
# Complex numbers comparison
assert cmath.isclose(complex(0.3, 0.1), complex(0.1 + 0.2, 0.1), abs_tol=1e-9)
Ecosystem-specific alternatives
import numpy as np
arr1 = np.sum(np.array([0.1, 0.2]))
assert np.all(arr1 == 0.3)  # AssertionError
```
## Use instead:
```
import numpy as np
arr1 = np.sum(np.array([0.1, 0.2]))
assert np.all(np.isclose(arr1, 0.3, rtol=1e-9, atol=1e-9))
# or
assert np.allclose(arr1, 0.3, rtol=1e-9, atol=1e-9)
```