# indentation-with-invalid-multiple (E111)
Derived from the pycodestyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for indentation with a non-multiple of 4 spaces.
## Why is this bad?
According to PEP 8, 4 spaces per indentation level should be preferred.
## Example
```
if True:
   a = 1
```
## Use instead:
```
if True:
    a = 1
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter enforces consistent indentation, making the rule redundant.
The rule is also incompatible with the formatter when using
indent-width with a value other than 4.
```