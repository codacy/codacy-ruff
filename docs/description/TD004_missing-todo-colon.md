# missing-todo-colon (TD004)
Derived from the flake8-todos linter.
## What it does
Checks that a "TODO" tag is followed by a colon.
## Why is this bad?
"TODO" tags are typically followed by a parenthesized author name, a colon,
a space, and a description of the issue, in that order.
Deviating from this pattern can lead to inconsistent and non-idiomatic
comments.
## Example
```
# TODO(charlie) fix this colon
Used instead:
# TODO(charlie): colon fixed
```