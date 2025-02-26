# self-assigning-variable (PLW0127)
Derived from the Pylint linter.
## What it does
Checks for self-assignment of variables.
## Why is this bad?
Self-assignment of variables is redundant and likely a mistake.
## Example
```
country = "Poland"
country = country
```
## Use instead:
```
country = "Poland"
```