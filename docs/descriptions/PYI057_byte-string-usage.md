# byte-string-usage (PYI057)
Derived from the flake8-pyi linter.
## What it does
Checks for uses of typing.ByteString or collections.abc.ByteString.
## Why is this bad?
ByteString has been deprecated since Python 3.9 and will be removed in
Python 3.14. The Python documentation recommends using either
collections.abc.Buffer (or the typing_extensions backport
on Python \<3.12) or a union like bytes | bytearray | memoryview instead.
## Example
```
from typing import ByteString
```
## Use instead:
```
from collections.abc import Buffer
```