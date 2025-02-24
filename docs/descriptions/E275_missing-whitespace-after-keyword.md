# missing-whitespace-after-keyword (E275)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing whitespace after keywords.
## Why is this bad?
Missing whitespace after keywords makes the code harder to read.
## Example
```
if(True):
    pass
```
## Use instead:
```
if (True):
    pass
```