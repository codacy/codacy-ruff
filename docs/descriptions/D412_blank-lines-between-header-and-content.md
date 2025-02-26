# blank-lines-between-header-and-content (D412)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstring sections that contain blank lines between a section
header and a section body.
## Why is this bad?
This rule enforces a consistent style for multiline docstrings.
Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body. There should be no blank lines between a section header
and a section body.
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