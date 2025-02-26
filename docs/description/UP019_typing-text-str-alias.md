# typing-text-str-alias (UP019)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for uses of typing.Text.
## Why is this bad?
typing.Text is an alias for str, and only exists for Python 2
compatibility. As of Python 3.11, typing.Text is deprecated. Use str
instead.
## Example
```
from typing import Text
foo: Text = "bar"
```
## Use instead:
```
foo: str = "bar"
```