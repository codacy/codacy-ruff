# hardcoded-string-charset (FURB156)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of hardcoded charsets, which are defined in Python string module.
## Why is this bad?
Usage of named charsets from the standard library is more readable and less error-prone.
## Example
```
x = "0123456789"
y in "abcdefghijklmnopqrstuvwxyz"
Use instead
import string
x = string.digits
y in string.ascii_lowercase
```