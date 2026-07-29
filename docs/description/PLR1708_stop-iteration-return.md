# stop-iteration-return (PLR1708)
Added in 0.16.0 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for explicit raise StopIteration in generator functions.
## Why is this bad?
Raising StopIteration in a generator function causes a RuntimeError
when the generator is iterated over.
Instead of raise StopIteration, use return in generator functions.
## Example
```
def my_generator():
    yield 1
    yield 2
    raise StopIteration  # This causes RuntimeError at runtime
```
## Use instead:
```
def my_generator():
    yield 1
    yield 2
    return  # Use return instead
```