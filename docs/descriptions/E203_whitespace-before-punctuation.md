# whitespace-before-punctuation (E203)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for the use of extraneous whitespace before ",", ";" or ":".
## Why is this bad?
PEP 8 recommends the omission of whitespace in the following cases:
"Immediately inside parentheses, brackets or braces."
"Immediately before a comma, semicolon, or colon."
## Example
```
if x == 4: print(x, y); x, y = y , x
```
## Use instead:
```
if x == 4: print(x, y); x, y = y, x
```