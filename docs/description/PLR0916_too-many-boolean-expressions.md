# too-many-boolean-expressions (PLR0916)
Preview (since v0.1.1) ·
Related issues ·
View source
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for too many Boolean expressions in an if statement.
By default, this rule allows up to 5 expressions. This can be configured
using the lint.pylint.max-bool-expr option.
## Why is this bad?
if statements with many Boolean expressions are harder to understand
and maintain. Consider assigning the result of the Boolean expression,
or any of its sub-expressions, to a variable.
## Example
```
if a and b and c and d and e and f and g and h:
    ...
```