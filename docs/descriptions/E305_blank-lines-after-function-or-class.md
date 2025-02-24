# blank-lines-after-function-or-class (E305)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for missing blank lines after the end of function or class.
## Why is this bad?
PEP 8 recommends using blank lines as follows:
Two blank lines are expected between functions and classes
One blank line is expected between methods of a class.
## Example
```
class User(object):
    pass
user = User()
```
## Use instead:
```
class User(object):
    pass
user = User()
Typing stub files (.pyi)
The typing style guide recommends to not use blank lines between statements except to group
them. That's why this rule is not enabled in typing stub files.
```