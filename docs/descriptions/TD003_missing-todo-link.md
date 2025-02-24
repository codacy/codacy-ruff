# missing-todo-link (TD003)
Derived from the flake8-todos linter.
## What it does
Checks that a TODO comment is associated with a link to a relevant issue
or ticket.
## Why is this bad?
Including an issue link near a TODO makes it easier for resolvers
to get context around the issue.
## Example
```
# TODO: this link has no issue
Use one of these instead:
# TODO(charlie): this comment has an issue link
# https://github.com/astral-sh/ruff/issues/3870
# TODO(charlie): this comment has a 3-digit issue code
# 003
# TODO(charlie): https://github.com/astral-sh/ruff/issues/3870
# this comment has an issue link
# TODO(charlie): #003 this comment has a 3-digit issue code
# with leading character `#`
# TODO(charlie): this comment has an issue code (matches the regex `[A-Z]+\-?\d+`)
# SIXCHR-003
```