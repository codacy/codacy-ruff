# collection-literal-concatenation (RUF005)
Fix is sometimes available.
## What it does
Checks for uses of the + operator to concatenate collections.
## Why is this bad?
In Python, the + operator can be used to concatenate collections (e.g.,
x + y to concatenate the lists x and y).
However, collections can be concatenated more efficiently using the
unpacking operator (e.g., [*x, *y] to concatenate x and y).
Prefer the unpacking operator to concatenate collections, as it is more
readable and flexible. The * operator can unpack any iterable, whereas
+ operates only on particular sequences which, in many cases, must be of
the same type.
## Example
```
foo = [2, 3, 4]
bar = [1] + foo + [5, 6]
```
## Use instead:
```
foo = [2, 3, 4]
bar = [1, *foo, 5, 6]
```