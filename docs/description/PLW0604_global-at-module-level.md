# global-at-module-level (PLW0604)
Derived from the Pylint linter.
## What it does
Checks for uses of the global keyword at the module level.
## Why is this bad?
The global keyword is used within functions to indicate that a name
refers to a global variable, rather than a local variable.
At the module level, all names are global by default, so the global
keyword is redundant.
```