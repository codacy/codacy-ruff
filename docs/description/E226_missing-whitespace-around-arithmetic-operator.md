# missing-whitespace-around-arithmetic-operator (E226)
Preview (since v0.0.269) ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace arithmetic operators.
## Why is this bad?
PEP 8 recommends never using more than one space, and always having the
same amount of whitespace on both sides of a binary operator.
For consistency, this rule enforces one space before and after an
arithmetic operator (+, -, /, and *).
(Note that PEP 8 suggests only adding whitespace around the operator with
the lowest precedence, but that authors should "use [their] own judgment".)
## Example
```
number = 40+2
```
## Use instead:
```
number = 40 + 2
```