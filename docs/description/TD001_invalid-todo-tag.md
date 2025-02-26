# invalid-todo-tag (TD001)
Derived from the flake8-todos linter.
## What it does
Checks that a TODO comment is labelled with "TODO".
## Why is this bad?
Ambiguous tags reduce code visibility and can lead to dangling TODOs.
For example, if a comment is tagged with "FIXME" rather than "TODO", it may
be overlooked by future readers.
Note that this rule will only flag "FIXME" and "XXX" tags as incorrect.
## Example
```
# FIXME(ruff): this should get fixed!
```
## Use instead:
```
# TODO(ruff): this is now fixed!
```