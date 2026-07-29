# tab-after-comma (E242)
Preview (since v0.0.281) ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous tabs after a comma.
## Why is this bad?
Commas should be followed by one space, never tabs.
## Example
```
a = 4,\t5
```
## Use instead:
```
a = 4, 5
```