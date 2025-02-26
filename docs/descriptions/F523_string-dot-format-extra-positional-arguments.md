# string-dot-format-extra-positional-arguments (F523)
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for str.format calls with unused positional arguments.
## Why is this bad?
Unused positional arguments are redundant, and often indicative of a mistake.
They should be removed.
## Example
```
"Hello, {0}".format("world", "!")
```
## Use instead:
```
"Hello, {0}".format("world")
```