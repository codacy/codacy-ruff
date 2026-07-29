# property-without-return (RUF066)
Preview (since 0.14.7) ·
Related issues ·
View source
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Detects class @property methods that does not have a return statement.
## Why is this bad?
Property methods are expected to return a computed value, a missing return in a property usually indicates an implementation mistake.
## Example
```
class User:
    @property
    def full_name(self):
        f"{self.first_name} {self.last_name}"
```
## Use instead:
```
class User:
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```