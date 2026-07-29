# too-many-statements-in-try-clause (PLW0717)
Preview (since 0.15.14) ·
Related issues ·
View source
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for try clauses with too many statements.
By default, this rule allows up to 5 statements, as configured by the
lint.pylint.max-statements-in-try option.
## Why is this bad?
Try clauses with many statements make unexpected exceptions harder
to detect and debug.
Instead, consider narrowing the try clause to only encompass code that
may raise exceptions you can anticipate or know about, moving all other
statements either before or after the try clause, or factoring out a helper function.
## Example
```
from random import randint
def random_ratio() -> float:
    try:
        a = randint(-100, 100)
        b = randint(-100, 100)
        c = randint(-100, 100)
        d = randint(-100, 100)
        scale = randint(1, 5)
        res = scale * (a + b) / (c + d)
    except ZeroDivisionError:
        return random_ratio()
    else:
        return res
```
## Use instead:
```
from random import randint
def random_ratio() -> float:
    a = randint(-100, 100)
    b = randint(-100, 100)
    c = randint(-100, 100)
    d = randint(-100, 100)
    scale = randint(1, 5)
    try:
        # every statement that cannot raise was moved outside the try clause
        res = scale * (a + b) / (c + d)
    except ZeroDivisionError:
        return random_ratio()
    else:
        return res
```