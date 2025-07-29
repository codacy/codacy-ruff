# trailing-whitespace (W291)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for superfluous trailing whitespace.
## Why is this bad?
According to PEP 8, "avoid trailing whitespace anywhere. Because it’s usually
invisible, it can be confusing"
## Example
```
spam(1) \n#
```
## Use instead:
```
spam(1)\n#
Fix safety
This fix is marked unsafe if the whitespace is inside a multiline string,
as removing it changes the string's content.
```