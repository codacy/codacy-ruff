# unspecified-encoding (PLW1514)
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of open and related calls without an explicit encoding
argument.
## Why is this bad?
Using open in text mode without an explicit encoding can lead to
non-portable code, with differing behavior across platforms. While readers
may assume that UTF-8 is the default encoding, in reality, the default
is locale-specific.
Instead, consider using the encoding parameter to enforce a specific
encoding. PEP 597 recommends the use of encoding="utf-8" as a default,
and suggests that it may become the default in future versions of Python.
If a locale-specific encoding is intended, use encoding="locale" on
Python 3.10 and later, or locale.getpreferredencoding() on earlier versions,
to make the encoding explicit.
## Example
```
open("file.txt")
```
## Use instead:
```
open("file.txt", encoding="utf-8")
```