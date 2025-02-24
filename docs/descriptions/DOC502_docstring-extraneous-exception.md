# docstring-extraneous-exception (DOC502)
Derived from the pydoclint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for function docstrings that state that exceptions could be raised
even though they are not directly raised in the function body.
## Why is this bad?
Some conventions prefer non-explicit exceptions be omitted from the
docstring.
This rule is not enforced for abstract methods. It is also ignored for
"stub functions": functions where the body only consists of pass, ...,
raise NotImplementedError, or similar.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Args:
        distance: Distance traveled.
        time: Time spent traveling.
    Returns:
        Speed as distance divided by time.
    Raises:
        ZeroDivisionError: Divided by zero.
    """
    return distance / time
```
## Use instead:
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Args:
        distance: Distance traveled.
        time: Time spent traveling.
    Returns:
        Speed as distance divided by time.
    """
    return distance / time
Known issues
It may often be desirable to document all exceptions that a function
could possibly raise, even those which are not explicitly raised using
raise statements in the function body.
```