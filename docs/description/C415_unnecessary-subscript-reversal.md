# unnecessary-subscript-reversal (C415)
Added in v0.0.64 ·
Related issues ·
View source
Derived from the flake8-comprehensions linter.
## What it does
Checks for unnecessary subscript reversal of iterable.
## Why is this bad?
It's unnecessary to reverse the order of an iterable when passing it
into reversed(), set() or sorted() functions as they will change
the order of the elements again.
## Example
```
sorted(iterable[::-1])
set(iterable[::-1])
reversed(iterable[::-1])
```
## Use instead:
```
sorted(iterable)
set(iterable)
iterable
```