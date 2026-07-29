# string-dot-format-invalid-format (F521)
Added in v0.0.138 ·
Related issues ·
View source
Derived from the Pyflakes linter.
## What it does
Checks for str.format calls with invalid format strings.
## Why is this bad?
Invalid format strings will raise a ValueError.
## Example
```
"{".format(foo)
```
## Use instead:
```
"{}".format(foo)
```