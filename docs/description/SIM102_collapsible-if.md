# collapsible-if (SIM102)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for nested if statements that can be collapsed into a single if
statement.
## Why is this bad?
Nesting if statements leads to deeper indentation and makes code harder to
read. Instead, combine the conditions into a single if statement with an
and operator.
## Example
```
if foo:
    if bar:
        ...
```
## Use instead:
```
if foo and bar:
    ...
```