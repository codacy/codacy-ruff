# whitespace-before-parameters (E211)
Preview (since v0.0.269) ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous whitespace immediately preceding an open parenthesis
or bracket.
## Why is this bad?
According to PEP 8, open parentheses and brackets should not be preceded
by any trailing whitespace.
## Example
```
spam (1)
```
## Use instead:
```
spam(1)
```