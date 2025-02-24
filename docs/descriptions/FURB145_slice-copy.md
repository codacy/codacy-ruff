# slice-copy (FURB145)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for unbounded slice expressions to copy a list.
## Why is this bad?
The list.copy method is more readable and consistent with copying other
types.
Known problems
This rule is prone to false negatives due to type inference limitations,
as it will only detect lists that are instantiated as literals or annotated
with a type annotation.
## Example
```
a = [1, 2, 3]
b = a[:]
```
## Use instead:
```
a = [1, 2, 3]
b = a.copy()
```