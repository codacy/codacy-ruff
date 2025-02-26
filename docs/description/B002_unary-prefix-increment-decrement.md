# unary-prefix-increment-decrement (B002)
Derived from the flake8-bugbear linter.
## What it does
Checks for the attempted use of the unary prefix increment (++) or
decrement operator (--).
## Why is this bad?
Python does not support the unary prefix increment or decrement operator.
Writing ++n is equivalent to +(+(n)) and writing --n is equivalent to
-(-(n)). In both cases, it is equivalent to n.
## Example
```
++x
--y
```
## Use instead:
```
x += 1
y -= 1
```