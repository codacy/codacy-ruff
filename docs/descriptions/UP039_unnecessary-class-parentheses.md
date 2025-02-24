# unnecessary-class-parentheses (UP039)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for class definitions that include unnecessary parentheses after
the class name.
## Why is this bad?
If a class definition doesn't have any bases, the parentheses are
unnecessary.
## Examples
```
class Foo():
    ...
```
## Use instead:
```
class Foo:
    ...
```