# collapsible-if (SIM102)
Added in v0.0.211 ·
Related issues ·
View source
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
Preview and Fix Safety
When preview is enabled, the fix for this rule is considered
as safe. When preview is not enabled, the fix is always
considered unsafe.
```