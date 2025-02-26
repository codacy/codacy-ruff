# none-comparison (E711)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for comparisons to None which are not using the is operator.
## Why is this bad?
According to PEP 8, "Comparisons to singletons like None should always be done with
is or is not, never the equality operators."
## Example
```
if arg != None:
    pass
if None == arg:
    pass
```
## Use instead:
```
if arg is not None:
    pass
Fix safety
This rule's fix is marked as unsafe, as it may alter runtime behavior when
used with libraries that override the ==/__eq__ or !=/__ne__ operators.
In these cases, is/is not may not be equivalent to ==/!=. For more
information, see this issue.
```