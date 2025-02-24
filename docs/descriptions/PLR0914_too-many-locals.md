# too-many-locals (PLR0914)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for functions that include too many local variables.
By default, this rule allows up to fifteen locals, as configured by the
lint.pylint.max-locals option.
## Why is this bad?
Functions with many local variables are harder to understand and maintain.
Consider refactoring functions with many local variables into smaller
functions with fewer assignments.
```