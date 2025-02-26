# percent-format-star-requires-sequence (F508)
Derived from the Pyflakes linter.
## What it does
Checks for printf-style format strings that use the * specifier with
non-tuple values.
## Why is this bad?
The use of the * specifier with non-tuple values will raise a
TypeError at runtime.
## Example
```
from math import pi
"%(n).*f" % {"n": (2, pi)}
```
## Use instead:
```
from math import pi
"%.*f" % (2, pi)  # 3.14
```