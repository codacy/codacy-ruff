# invalid-index-type (RUF016)
## What it does
Checks for indexed access to lists, strings, tuples, bytes, and comprehensions
using a type other than an integer or slice.
## Why is this bad?
Only integers or slices can be used as indices to these types. Using
other types will result in a TypeError at runtime and a SyntaxWarning at
import time.
## Example
```
var = [1, 2, 3]["x"]
```
## Use instead:
```
var = [1, 2, 3][0]
```