# if-expr-with-false-true (SIM211)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for if expressions that can be replaced by negating a given
condition.
## Why is this bad?
if expressions that evaluate to False for a truthy condition and True
for a falsey condition can be replaced with not operators, which are more
concise and readable.
## Example
```
False if a else True
```
## Use instead:
```
not a
```