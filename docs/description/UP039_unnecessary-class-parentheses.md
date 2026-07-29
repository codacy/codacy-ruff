# unnecessary-class-parentheses (UP039)
Added in v0.0.273 ·
Related issues ·
View source
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for class definitions that include unnecessary parentheses after
the class name.
## Why is this bad?
If a class definition doesn't have any bases, the parentheses are
unnecessary.
## Example
```
class Foo():
    ...
```
## Use instead:
```
class Foo:
    ...
Fix safety
This rule's fix is marked as unsafe if it would delete any comments
within the parentheses range.
```