# if-expr-with-true-false (SIM210)
Derived from the flake8-simplify linter.
Fix is sometimes available.
## What it does
Checks for if expressions that can be replaced with bool() calls.
## Why is this bad?
if expressions that evaluate to True for a truthy condition an False
for a falsey condition can be replaced with bool() calls, which are more
concise and readable.
## Example
```
True if a else False
```
## Use instead:
```
bool(a)
```