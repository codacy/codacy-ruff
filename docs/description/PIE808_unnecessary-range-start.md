# unnecessary-range-start (PIE808)
Added in v0.0.286 ·
Related issues ·
View source
Derived from the flake8-pie linter.
Fix is always available.
## What it does
Checks for range calls with an unnecessary start argument.
## Why is this bad?
range(0, x) is equivalent to range(x), as 0 is the default value for
the start argument. Omitting the start argument makes the code more
concise and idiomatic.
## Example
```
range(0, 3)
```
## Use instead:
```
range(3)
```