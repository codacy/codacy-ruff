# non-capitalized-section-name (D405)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for section headers in docstrings that do not begin with capital
letters.
## Why is this bad?
For stylistic consistency, all section headers in a docstring should be
capitalized.
Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections. Each section typically has
a header and a body.
This rule is enabled when using the numpy and google conventions, and
disabled when using the pep257 convention.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    args:
        distance: Distance traveled.
        time: Time spent traveling.
    returns:
        Speed as distance divided by time.
    raises:
        FasterThanLightError: If speed is greater than the speed of light.
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