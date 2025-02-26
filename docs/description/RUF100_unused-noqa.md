# unused-noqa (RUF100)
Fix is always available.
## What it does
Checks for noqa directives that are no longer applicable.
## Why is this bad?
A noqa directive that no longer matches any diagnostic violations is
likely included by mistake, and should be removed to avoid confusion.
## Example
```
import foo  # noqa: F401
def bar():
    foo.bar()
```
## Use instead:
```
import foo
def bar():
    foo.bar()
```