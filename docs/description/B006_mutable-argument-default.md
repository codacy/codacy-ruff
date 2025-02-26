# mutable-argument-default (B006)
Derived from the flake8-bugbear linter.
Fix is sometimes available.
## What it does
Checks for uses of mutable objects as function argument defaults.
## Why is this bad?
Function defaults are evaluated once, when the function is defined.
The same mutable object is then shared across all calls to the function.
If the object is modified, those modifications will persist across calls,
which can lead to unexpected behavior.
Instead, prefer to use immutable data structures, or take None as a
default, and initialize a new mutable object inside the function body
for each call.
Arguments with immutable type annotations will be ignored by this rule.
Types outside of the standard library can be marked as immutable with the
lint.flake8-bugbear.extend-immutable-calls configuration option.
Known problems
Mutable argument defaults can be used intentionally to cache computation
results. Replacing the default with None or an immutable data structure
does not work for such usages. Instead, prefer the @functools.lru_cache
decorator from the standard library.
## Example
```
def add_to_list(item, some_list=[]):
    some_list.append(item)
    return some_list
l1 = add_to_list(0)  # [0]
l2 = add_to_list(1)  # [0, 1]
```
## Use instead:
```
def add_to_list(item, some_list=None):
    if some_list is None:
        some_list = []
    some_list.append(item)
    return some_list
l1 = add_to_list(0)  # [0]
l2 = add_to_list(1)  # [1]
```