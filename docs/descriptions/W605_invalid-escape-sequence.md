# invalid-escape-sequence (W605)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for invalid escape sequences.
## Why is this bad?
Invalid escape sequences are deprecated in Python 3.6.
## Example
```
regex = "\.png$"
```
## Use instead:
```
regex = r"\.png$"
Or, if the string already contains a valid escape sequence:
value = "new line\nand invalid escape \_ here"
```
## Use instead:
```
value = "new line\nand invalid escape \\_ here"
```