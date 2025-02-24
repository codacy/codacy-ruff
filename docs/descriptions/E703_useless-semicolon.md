# useless-semicolon (E703)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for statements that end with an unnecessary semicolon.
## Why is this bad?
A trailing semicolon is unnecessary and should be removed.
## Example
```
do_four();  # useless semicolon
```
## Use instead:
```
do_four()
```