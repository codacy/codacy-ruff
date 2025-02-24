# too-many-newlines-at-end-of-file (W391)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for files with multiple trailing blank lines.
In the case of notebooks, this check is applied to
each cell separately.
## Why is this bad?
Trailing blank lines in a file are superfluous.
However, the last line of the file should end with a newline.
## Example
```
spam(1)\n\n\n
```
## Use instead:
```
spam(1)\n
```