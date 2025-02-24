# over-indented (E117)
Derived from the pycodestyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for over-indented code.
## Why is this bad?
According to PEP 8, 4 spaces per indentation level should be preferred. Increased
indentation can lead to inconsistent formatting, which can hurt
readability.
## Example
```
for item in items:
      pass
```
## Use instead:
```
for item in items:
    pass
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter enforces consistent indentation, making the rule redundant.
```