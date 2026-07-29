# missing-newline-at-end-of-file (W292)
Added in v0.0.61 ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for files missing a new line at the end of the file.
## Why is this bad?
Trailing blank lines in a file are superfluous.
However, the last line of the file should end with a newline.
## Example
```
spam(1)
```
## Use instead:
```
spam(1)\n
```