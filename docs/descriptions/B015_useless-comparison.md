# useless-comparison (B015)
Derived from the flake8-bugbear linter.
## What it does
Checks for useless comparisons.
## Why is this bad?
Useless comparisons have no effect on the program, and are often included
by mistake. If the comparison is intended to enforce an invariant, prepend
the comparison with an assert. Otherwise, remove it entirely.
## Example
```
foo == bar
```
## Use instead:
```
assert foo == bar, "`foo` and `bar` should be equal."
Notebook behavior
For Jupyter Notebooks, this rule is not applied to the last top-level expression in a cell.
This is because it's common to have a notebook cell that ends with an expression,
which will result in the repr of the evaluated expression being printed as the cell's output.
```