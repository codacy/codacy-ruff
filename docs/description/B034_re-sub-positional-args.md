# re-sub-positional-args (B034)
Derived from the flake8-bugbear linter.
## What it does
Checks for calls to re.sub, re.subn, and re.split that pass count,
maxsplit, or flags as positional arguments.
## Why is this bad?
Passing count, maxsplit, or flags as positional arguments to
re.sub, re.subn, or re.split can lead to confusion, as most methods in
the re module accept flags as the third positional argument, while
re.sub, re.subn, and re.split have different signatures.
Instead, pass count, maxsplit, and flags as keyword arguments.
## Example
```
import re
re.split("pattern", "replacement", 1)
```
## Use instead:
```
import re
re.split("pattern", "replacement", maxsplit=1)
```