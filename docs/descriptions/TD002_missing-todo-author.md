# missing-todo-author (TD002)
Derived from the flake8-todos linter.
## What it does
Checks that a TODO comment includes an author.
## Why is this bad?
Including an author on a TODO provides future readers with context around
the issue. While the TODO author is not always considered responsible for
fixing the issue, they are typically the individual with the most context.
## Example
```
# TODO: should assign an author here
Use instead
# TODO(charlie): now an author is assigned
```