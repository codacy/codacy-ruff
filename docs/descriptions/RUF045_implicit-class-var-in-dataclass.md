# implicit-class-var-in-dataclass (RUF045)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for implicit class variables in dataclasses.
Variables matching the lint.dummy-variable-rgx are excluded
from this rule.
## Why is this bad?
Class variables are shared between all instances of that class.
In dataclasses, fields with no annotations at all
are implicitly considered class variables, and a TypeError is
raised if a user attempts to initialize an instance of the class
with this field.
@dataclass
class C:
    a = 1
    b: str = ""
C(a = 42)  # TypeError: C.__init__() got an unexpected keyword argument 'a'
## Example
```
@dataclass
class C:
    a = 1
```
## Use instead:
```
from typing import ClassVar
@dataclass
class C:
    a: ClassVar[int] = 1
```