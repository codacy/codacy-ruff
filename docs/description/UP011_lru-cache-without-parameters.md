# lru-cache-without-parameters (UP011)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary parentheses on functools.lru_cache decorators.
## Why is this bad?
Since Python 3.8, functools.lru_cache can be used as a decorator without
trailing parentheses, as long as no arguments are passed to it.
## Example
```
import functools
@functools.lru_cache()
def foo(): ...
```
## Use instead:
```
import functools
@functools.lru_cache
def foo(): ...
```