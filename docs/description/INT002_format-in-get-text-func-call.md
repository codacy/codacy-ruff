# format-in-get-text-func-call (INT002)
Derived from the flake8-gettext linter.
## What it does
Checks for str.format calls in gettext function calls.
## Why is this bad?
In the gettext API, the gettext function (often aliased to _) returns
a translation of its input argument by looking it up in a translation
catalog.
Calling gettext with a formatted string as its argument can cause
unexpected behavior. Since the formatted string is resolved before the
function call, the translation catalog will look up the formatted string,
rather than the str.format-style template.
Instead, format the value returned by the function call, rather than
its argument.
## Example
```
from gettext import gettext as _
name = "Maria"
_("Hello, {}!".format(name))  # Looks for "Hello, Maria!".
```
## Use instead:
```
from gettext import gettext as _
name = "Maria"
_("Hello, %s!") % name  # Looks for "Hello, %s!".
```