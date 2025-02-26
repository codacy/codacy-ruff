# function-uses-loop-variable (B023)
Derived from the flake8-bugbear linter.
## What it does
Checks for function definitions that use a loop variable.
## Why is this bad?
The loop variable is not bound in the function definition, so it will always
have the value it had in the last iteration when the function is called.
Instead, consider using a default argument to bind the loop variable at
function definition time. Or, use functools.partial.
## Example
```
adders = [lambda x: x + i for i in range(3)]
values = [adder(1) for adder in adders]  # [3, 3, 3]
```
## Use instead:
```
adders = [lambda x, i=i: x + i for i in range(3)]
values = [adder(1) for adder in adders]  # [1, 2, 3]
Or:
from functools import partial
adders = [partial(lambda x, i: x + i, i=i) for i in range(3)]
values = [adder(1) for adder in adders]  # [1, 2, 3]
```