# unnecessary-comprehension (C416)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary dict, list, and set comprehension.
## Why is this bad?
It's unnecessary to use a dict/list/set comprehension to build a data structure if the
elements are unchanged. Wrap the iterable with dict(), list(), or set() instead.
## Examples
```
{a: b for a, b in iterable}
[x for x in iterable]
{x for x in iterable}
```
## Use instead:
```
dict(iterable)
list(iterable)
set(iterable)
Known problems
This rule may produce false positives for dictionary comprehensions that iterate over a mapping.
The dict constructor behaves differently depending on if it receives a sequence (e.g., a
list) or a mapping (e.g., a dict). When a comprehension iterates over the keys of a mapping,
replacing it with a dict() constructor call will give a different result.
For example:
>>> d1 = {(1, 2): 3, (4, 5): 6}
>>> {x: y for x, y in d1}  # Iterates over the keys of a mapping
{1: 2, 4: 5}
>>> dict(d1)               # Ruff's incorrect suggested fix
(1, 2): 3, (4, 5): 6}
>>> dict(d1.keys())        # Correct fix
{1: 2, 4: 5}
When the comprehension iterates over a sequence, Ruff's suggested fix is correct. However, Ruff
cannot consistently infer if the iterable type is a sequence or a mapping and cannot suggest
the correct fix for mappings.
Fix safety
Due to the known problem with dictionary comprehensions, this fix is marked as unsafe.
Additionally, this fix may drop comments when rewriting the comprehension.
```