# parenthesize-chained-operators (RUF021)
Fix is always available.
## What it does
Checks for chained operators where adding parentheses could improve the
clarity of the code.
## Why is this bad?
and always binds more tightly than or when chaining the two together,
but this can be hard to remember (and sometimes surprising).
Adding parentheses in these situations can greatly improve code readability,
with no change to semantics or performance.
For example:
a, b, c = 1, 0, 2
x = a or b and c
d, e, f = 0, 1, 2
y = d and e or f
```
## Use instead:
```
a, b, c = 1, 0, 2
x = a or (b and c)
d, e, f = 0, 1, 2
y = (d and e) or f
```