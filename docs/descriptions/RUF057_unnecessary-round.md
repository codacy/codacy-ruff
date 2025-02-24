# unnecessary-round (RUF057)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for round() calls that have no effect on the input.
## Why is this bad?
Rounding a value that's already an integer is unnecessary.
It's clearer to use the value directly.
## Example
```
a = round(1, 0)
```
## Use instead:
```
a = 1
```