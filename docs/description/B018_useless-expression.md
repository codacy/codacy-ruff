# useless-expression (B018)
Derived from the flake8-bugbear linter.
## What it does
Checks for useless expressions.
## Why is this bad?
Useless expressions have no effect on the program, and are often included
by mistake. Assign a useless expression to a variable, or remove it
entirely.
## Example
```
1 + 1
```
## Use instead:
```
foo = 1 + 1
Notebook behavior
For Jupyter Notebooks, this rule is not applied to the last top-level expression in a cell.
This is because it's common to have a notebook cell that ends with an expression,
which will result in the repr of the evaluated expression being printed as the cell's output.
Known problems
This rule ignores expression types that are commonly used for their side
effects, such as function calls.
However, if a seemingly useless expression (like an attribute access) is
needed to trigger a side effect, consider assigning it to an anonymous
variable, to indicate that the return value is intentionally ignored.
For example, given:
with errors.ExceptionRaisedContext():
    obj.attribute
```
## Use instead:
```
with errors.ExceptionRaisedContext():
    _ = obj.attribute
```