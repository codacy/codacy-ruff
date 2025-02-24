# needless-else (RUF047)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for else clauses that only contains pass and ... statements.
## Why is this bad?
Such an else clause does nothing and can be removed.
## Example
```
if foo:
    bar()
else:
    pass
```
## Use instead:
```
if foo:
    bar()
```