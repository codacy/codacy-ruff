# missing-space-after-todo-colon (TD007)
Added in v0.0.269 ·
Related issues ·
View source
Derived from the flake8-todos linter.
## What it does
Checks that the colon after a "TODO" tag is followed by a space.
## Why is this bad?
"TODO" tags are typically followed by a parenthesized author name, a colon,
a space, and a description of the issue, in that order.
Deviating from this pattern can lead to inconsistent and non-idiomatic
comments.
## Example
```
# TODO(charlie):fix this
```
## Use instead:
```
# TODO(charlie): fix this
```