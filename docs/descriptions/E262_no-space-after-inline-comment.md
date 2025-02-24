# no-space-after-inline-comment (E262)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks if one space is used after inline comments.
## Why is this bad?
An inline comment is a comment on the same line as a statement.
Per PEP 8, inline comments should start with a # and a single space.
## Example
```
x = x + 1  #Increment x
x = x + 1  #  Increment x
x = x + 1  # \xa0Increment x
```
## Use instead:
```
x = x + 1  # Increment x
x = x + 1    # Increment x
```