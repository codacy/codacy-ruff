# cached-instance-method (B019)
Derived from the flake8-bugbear linter.
## What it does
Checks for uses of the functools.lru_cache and functools.cache
decorators on methods.
## Why is this bad?
Using the functools.lru_cache and functools.cache decorators on methods
can lead to memory leaks, as the global cache will retain a reference to
the instance, preventing it from being garbage collected.
Instead, refactor the method to depend only on its arguments and not on the
instance of the class, or use the @lru_cache decorator on a function
outside of the class.
This rule ignores instance methods on enumeration classes, as enum members
are singletons.
## Example
```
from functools import lru_cache
def square(x: int) -> int:
    return x * x
class Number:
    value: int
    @lru_cache
    def squared(self):
        return square(self.value)
```
## Use instead:
```
from functools import lru_cache
@lru_cache
def square(x: int) -> int:
    return x * x
class Number:
    value: int
    def squared(self):
        return square(self.value)
```