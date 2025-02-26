# missing-todo-description (TD005)
Derived from the flake8-todos linter.
## What it does
Checks that a "TODO" tag contains a description of the issue following the
tag itself.
## Why is this bad?
TODO comments should include a description of the issue to provide context
for future readers.
## Example
```
# TODO(charlie)
```
## Use instead:
```
# TODO(charlie): fix some issue
```