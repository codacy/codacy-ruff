# f-string (UP032)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for str.format calls that can be replaced with f-strings.
## Why is this bad?
f-strings are more readable and generally preferred over str.format
calls.
## Example
```
"{}".format(foo)
```
## Use instead:
```
f"{foo}"
```