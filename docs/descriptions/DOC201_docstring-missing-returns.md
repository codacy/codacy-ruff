# docstring-missing-returns (DOC201)
Derived from the pydoclint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for functions with return statements that do not have "Returns"
sections in their docstrings.
## Why is this bad?
A missing "Returns" section is a sign of incomplete documentation.
This rule is not enforced for abstract methods or functions that only return
None. It is also ignored for "stub functions": functions where the body only
consists of pass, ..., raise NotImplementedError, or similar.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Args:
        distance: Distance traveled.
        time: Time spent traveling.
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
```