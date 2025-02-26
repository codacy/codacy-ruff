# lru-cache-with-maxsize-none (UP033)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of functools.lru_cache that set maxsize=None.
## Why is this bad?
Since Python 3.9, functools.cache can be used as a drop-in replacement
for functools.lru_cache(maxsize=None). When possible, prefer
functools.cache as it is more readable and idiomatic.
## Example
```
import functools
@functools.lru_cache(maxsize=None)
def foo(): ...
```
## Use instead:
```
import functools
@functools.cache
def foo(): ...
```