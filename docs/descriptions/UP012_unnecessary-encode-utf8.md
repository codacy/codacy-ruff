# unnecessary-encode-utf8 (UP012)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary calls to encode as UTF-8.
## Why is this bad?
UTF-8 is the default encoding in Python, so there is no need to call
encode when UTF-8 is the desired encoding. Instead, use a bytes literal.
## Example
```
"foo".encode("utf-8")
```
## Use instead:
```
b"foo"
```