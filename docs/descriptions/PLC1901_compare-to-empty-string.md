# compare-to-empty-string (PLC1901)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for comparisons to empty strings.
## Why is this bad?
An empty string is falsy, so it is unnecessary to compare it to "". If
the value can be something else Python considers falsy, such as None,
0, or another empty container, then the code is not equivalent.
Known problems
High false positive rate, as the check is context-insensitive and does not
consider the type of the variable being compared (#4282).
## Example
```
x: str = ...
if x == "":
    print("x is empty")
```
## Use instead:
```
x: str = ...
if not x:
    print("x is empty")
```