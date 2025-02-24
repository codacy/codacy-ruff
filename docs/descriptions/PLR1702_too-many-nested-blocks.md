# too-many-nested-blocks (PLR1702)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for functions or methods with too many nested blocks.
By default, this rule allows up to five nested blocks.
This can be configured using the lint.pylint.max-nested-blocks option.
## Why is this bad?
Functions or methods with too many nested blocks are harder to understand
and maintain.
```