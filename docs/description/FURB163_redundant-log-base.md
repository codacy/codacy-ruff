# redundant-log-base (FURB163)
Derived from the refurb linter.
Fix is sometimes available.
## What it does
Checks for math.log calls with a redundant base.
## Why is this bad?
The default base of math.log is e, so specifying it explicitly is
redundant.
Instead of passing 2 or 10 as the base, use math.log2 or math.log10
respectively, as these dedicated variants are typically more accurate
than math.log.
## Example
```
import math
math.log(4, math.e)
math.log(4, 2)
math.log(4, 10)
```
## Use instead:
```
import math
math.log(4)
math.log2(4)
math.log10(4)
```