# unnecessary-encode-utf8 (UP012)
Added in v0.0.155 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for unnecessary calls to encode as UTF-8 and unnecessary explicit
UTF-8 encoding arguments.
## Why is this bad?
UTF-8 is the default encoding in Python, so there is no need to pass an
explicit UTF-8 encoding to encode. For ASCII literals, use a bytes literal
instead; for other strings, omit the explicit encoding argument.
## Example
```
"foo".encode("utf-8")
"unicode text©".encode(encoding="utf-8")
```
## Use instead:
```
b"foo"
"unicode text©".encode()
```