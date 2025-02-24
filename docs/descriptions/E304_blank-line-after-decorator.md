# blank-line-after-decorator (E304)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous blank line(s) after function decorators.
## Why is this bad?
There should be no blank lines between a decorator and the object it is decorating.
## Example
```
class User(object):
    @property
    def name(self):
        pass
```
## Use instead:
```
class User(object):
    @property
    def name(self):
        pass
```