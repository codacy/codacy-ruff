# reimplemented-starmap (FURB140)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for generator expressions, list and set comprehensions that can
be replaced with itertools.starmap.
## Why is this bad?
When unpacking values from iterators to pass them directly to
a function, prefer itertools.starmap.
Using itertools.starmap is more concise and readable. Furthermore, it is
more efficient than generator expressions, and in some versions of Python,
it is more efficient than comprehensions.
Known problems
Since Python 3.12, itertools.starmap is less efficient than
comprehensions (#7771). This is due to PEP 709, which made
comprehensions faster.
## Example
```
all(predicate(a, b) for a, b in some_iterable)
```
## Use instead:
```
from itertools import starmap
all(starmap(predicate, some_iterable))
```