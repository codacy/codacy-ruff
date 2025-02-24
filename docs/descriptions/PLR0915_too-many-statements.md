# too-many-statements (PLR0915)
Derived from the Pylint linter.
## What it does
Checks for functions or methods with too many statements.
By default, this rule allows up to 50 statements, as configured by the
lint.pylint.max-statements option.
## Why is this bad?
Functions or methods with many statements are harder to understand
and maintain.
Instead, consider refactoring the function or method into smaller
functions or methods, or identifying generalizable patterns and
replacing them with generic logic or abstractions.
## Example
```
def is_even(number: int) -> bool:
    if number == 0:
        return True
    elif number == 1:
        return False
    elif number == 2:
        return True
    elif number == 3:
        return False
    elif number == 4:
        return True
    elif number == 5:
        return False
    else:
        ...
```
## Use instead:
```
def is_even(number: int) -> bool:
    return number % 2 == 0
```