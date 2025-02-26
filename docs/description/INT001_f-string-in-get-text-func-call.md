# f-string-in-get-text-func-call (INT001)
Derived from the flake8-gettext linter.
## What it does
Checks for f-strings in gettext function calls.
## Why is this bad?
In the gettext API, the gettext function (often aliased to _) returns
a translation of its input argument by looking it up in a translation
catalog.
Calling gettext with an f-string as its argument can cause unexpected
behavior. Since the f-string is resolved before the function call, the
translation catalog will look up the formatted string, rather than the
f-string template.
Instead, format the value returned by the function call, rather than
its argument.
## Example
```
from gettext import gettext as _
name = "Maria"
_(f"Hello, {name}!")  # Looks for "Hello, Maria!".
```
## Use instead:
```
from gettext import gettext as _
name = "Maria"
_("Hello, %s!") % name  # Looks for "Hello, %s!".
```