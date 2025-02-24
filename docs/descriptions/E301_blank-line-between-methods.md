# blank-line-between-methods (E301)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing blank lines between methods of a class.
## Why is this bad?
PEP 8 recommends exactly one blank line between methods of a class.
## Example
```
class MyClass(object):
    def func1():
        pass
    def func2():
        pass
```
## Use instead:
```
class MyClass(object):
    def func1():
        pass
    def func2():
        pass
Typing stub files (.pyi)
The typing style guide recommends to not use blank lines between methods except to group
them. That's why this rule is not enabled in typing stub files.
```