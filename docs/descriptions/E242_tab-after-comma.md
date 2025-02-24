# tab-after-comma (E242)
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