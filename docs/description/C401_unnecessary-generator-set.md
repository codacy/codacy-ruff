# unnecessary-generator-set (C401)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary generators that can be rewritten as set
comprehensions (or with set() directly).
## Why is this bad?
It is unnecessary to use set around a generator expression, since
there are equivalent comprehensions for these types. Using a
comprehension is clearer and more idiomatic.
Further, if the comprehension can be removed entirely, as in the case of
set(x for x in foo), it's better to use set(foo) directly, since it's
even more direct.
## Example
```
set(f(x) for x in foo)
set(x for x in foo)
set((x for x in foo))
```
## Use instead:
```
{f(x) for x in foo}
set(foo)
set(foo)
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```