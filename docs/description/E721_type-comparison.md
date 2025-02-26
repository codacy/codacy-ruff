# type-comparison (E721)
Derived from the pycodestyle linter.
## What it does
Checks for object type comparisons using == and other comparison
operators.
## Why is this bad?
Unlike a direct type comparison, isinstance will also check if an object
is an instance of a class or a subclass thereof.
If you want to check for an exact type match, use is or is not.
Known problems
When using libraries that override the == (__eq__) operator (such as NumPy,
Pandas, and SQLAlchemy), this rule may produce false positives, as converting
from == to is or is not will change the behavior of the code.
For example, the following operations are not equivalent:
import numpy as np
np.array([True, False]) == False
# array([False,  True])
np.array([True, False]) is False
# False
## Example
```
if type(obj) == type(1):
    pass
if type(obj) == int:
    pass
```
## Use instead:
```
if isinstance(obj, int):
    pass
```