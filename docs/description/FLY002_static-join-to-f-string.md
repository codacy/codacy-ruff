# static-join-to-f-string (FLY002)
Derived from the flynt linter.
Fix is always available.
## What it does
Checks for str.join calls that can be replaced with f-strings.
## Why is this bad?
f-strings are more readable and generally preferred over str.join calls.
## Example
```
" ".join((foo, bar))
```
## Use instead:
```
f"{foo} {bar}"
```