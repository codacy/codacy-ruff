# true-false-comparison (E712)
Derived from the pycodestyle linter.
Fix is always available.
## What it does
Checks for equality comparisons to boolean literals.
## Why is this bad?
PEP 8 recommends against using the equality operators == and != to
compare values to True or False.
Instead, use if cond: or if not cond: to check for truth values.
If you intend to check if a value is the boolean literal True or False,
consider using is or is not to check for identity instead.
## Example
```
if foo == True:
    ...
if bar == False:
    ...
```
## Use instead:
```
if foo:
    ...
if not bar:
    ...
Fix safety
This rule's fix is marked as unsafe, as it may alter runtime behavior when
used with libraries that override the ==/__eq__ or !=/__ne__ operators.
In these cases, is/is not may not be equivalent to ==/!=. For more
information, see this issue.
```