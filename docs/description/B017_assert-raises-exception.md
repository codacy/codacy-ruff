# assert-raises-exception (B017)
Added in v0.0.83 ·
Related issues ·
View source
Derived from the flake8-bugbear linter.
## What it does
Checks for assertRaises and pytest.raises context managers that catch
Exception or BaseException.
## Why is this bad?
These forms catch every Exception, which can lead to tests passing even
if, e.g., the code under consideration raises a SyntaxError or
IndentationError.
Either assert for a more specific exception (builtin or custom), or use
assertRaisesRegex or pytest.raises(..., match=<REGEX>) respectively.
## Example
```
self.assertRaises(Exception, foo)
```
## Use instead:
```
self.assertRaises(SomeSpecificException, foo)
```