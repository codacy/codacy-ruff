# blank-lines-before-nested-definition (E306)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for 1 blank line between nested function or class definitions.
## Why is this bad?
PEP 8 recommends using blank lines as follows:
Two blank lines are expected between functions and classes
One blank line is expected between methods of a class.
## Example
```
def outer():
    def inner():
        pass
    def inner2():
        pass
```
## Use instead:
```
def outer():
    def inner():
        pass
    def inner2():
        pass
Typing stub files (.pyi)
The typing style guide recommends to not use blank lines between classes and functions except to group
them. That's why this rule is not enabled in typing stub files.
```