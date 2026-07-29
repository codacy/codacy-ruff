# missing-whitespace-around-bitwise-or-shift-operator (E227)
Preview (since v0.0.269) ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace around bitwise and shift operators.
## Why is this bad?
PEP 8 recommends never using more than one space, and always having the
same amount of whitespace on both sides of a binary operator.
For consistency, this rule enforces one space before and after bitwise and
shift operators (<<, >>, &, |, ^).
(Note that PEP 8 suggests only adding whitespace around the operator with
the lowest precedence, but that authors should "use [their] own judgment".)
## Example
```
x = 128<<1
```
## Use instead:
```
x = 128 << 1
```