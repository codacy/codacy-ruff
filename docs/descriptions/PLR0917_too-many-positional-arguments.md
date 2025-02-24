# too-many-positional-arguments (PLR0917)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for function definitions that include too many positional arguments.
By default, this rule allows up to five arguments, as configured by the
lint.pylint.max-positional-args option.
## Why is this bad?
Functions with many arguments are harder to understand, maintain, and call.
This is especially true for functions with many positional arguments, as
providing arguments positionally is more error-prone and less clear to
readers than providing arguments by name.
Consider refactoring functions with many arguments into smaller functions
with fewer arguments, using objects to group related arguments, or migrating to
keyword-only arguments.
## Example
```
def plot(x, y, z, color, mark, add_trendline): ...
plot(1, 2, 3, "r", "*", True)
```
## Use instead:
```
def plot(x, y, z, *, color, mark, add_trendline): ...
plot(1, 2, 3, color="r", mark="*", add_trendline=True)
```