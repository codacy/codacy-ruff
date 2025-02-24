# docstring-missing-exception (DOC501)
Derived from the pydoclint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for function docstrings that do not document all explicitly raised
exceptions.
## Why is this bad?
A function should document all exceptions that are directly raised in some
circumstances. Failing to document an exception that could be raised
can be misleading to users and/or a sign of incomplete documentation.
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
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
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
    Raises:
        FasterThanLightError: If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```