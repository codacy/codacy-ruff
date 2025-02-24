# tab-before-keyword (E274)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous tabs before keywords.
## Why is this bad?
## Example
```
True\tand False
```
## Use instead:
```
True and False
```