# unnecessary-generator-dict (C402)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for unnecessary generators that can be rewritten as dict
comprehensions.
## Why is this bad?
It is unnecessary to use dict() around a generator expression, since
there are equivalent comprehensions for these types. Using a
comprehension is clearer and more idiomatic.
## Example
```
dict((x, f(x)) for x in foo)
```
## Use instead:
```
{x: f(x) for x in foo}
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```