# unnecessary-literal-within-dict-call (C418)
Derived from the flake8-comprehensions linter.
Fix is always available.
## What it does
Checks for dict() calls that take unnecessary dict literals or dict
comprehensions as arguments.
## Why is this bad?
It's unnecessary to wrap a dict literal or comprehension within a dict()
call, since the literal or comprehension syntax already returns a
dictionary.
## Examples
```
dict({})
dict({"a": 1})
```
## Use instead:
```
{}
{"a": 1}
Fix safety
This rule's fix is marked as unsafe, as it may occasionally drop comments
when rewriting the call. In most cases, though, comments will be preserved.
```