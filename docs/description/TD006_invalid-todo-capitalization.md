# invalid-todo-capitalization (TD006)
Derived from the flake8-todos linter.
Fix is always available.
## What it does
Checks that a "TODO" tag is properly capitalized (i.e., that the tag is
uppercase).
## Why is this bad?
Capitalizing the "TODO" in a TODO comment is a convention that makes it
easier for future readers to identify TODOs.
## Example
```
# todo(charlie): capitalize this
```
## Use instead:
```
# TODO(charlie): this is capitalized
```