# if-else-block-instead-of-if-exp (SIM108)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Check for if-else-blocks that can be replaced with a ternary
or binary operator.
The lint is suppressed if the suggested replacement would exceed
the maximum line length configured in pycodestyle.max-line-length.
## Why is this bad?
if-else-blocks that assign a value to a variable in both branches can
be expressed more concisely by using a ternary or binary operator.
## Example
```
if foo:
    bar = x
else:
    bar = y
```
## Use instead:
```
bar = x if foo else y
Or:
if cond:
    z = cond
else:
    z = other_cond
```
## Use instead:
```
z = cond or other_cond
Known issues
This is an opinionated style rule that may not always be to everyone's
taste, especially for code that makes use of complex if conditions.
Ternary operators can also make it harder to measure code coverage
with tools that use line profiling.
```