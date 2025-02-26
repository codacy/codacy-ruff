# mixed-spaces-and-tabs (E101)
Derived from the pycodestyle linter.
## What it does
Checks for mixed tabs and spaces in indentation.
## Why is this bad?
Never mix tabs and spaces.
The most popular way of indenting Python is with spaces only. The
second-most popular way is with tabs only. Code indented with a
mixture of tabs and spaces should be converted to using spaces
exclusively.
## Example
```
if a == 0:\n        a = 1\n\tb = 1
```
## Use instead:
```
if a == 0:\n    a = 1\n    b = 1
```