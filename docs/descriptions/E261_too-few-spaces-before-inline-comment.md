# too-few-spaces-before-inline-comment (E261)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks if inline comments are separated by at least two spaces.
## Why is this bad?
An inline comment is a comment on the same line as a statement.
Per PEP 8, inline comments should be separated by at least two spaces from
the preceding statement.
## Example
```
x = x + 1 # Increment x
```
## Use instead:
```
x = x + 1  # Increment x
x = x + 1    # Increment x
```