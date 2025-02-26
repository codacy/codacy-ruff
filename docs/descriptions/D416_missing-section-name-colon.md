# missing-section-name-colon (D416)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstring section headers that do not end with a colon.
## Why is this bad?
This rule enforces a consistent style for multiline Google-style
docstrings. If a multiline Google-style docstring consists of multiple
sections, each section header should end with a colon.
Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body.
This rule is enabled when using the google convention, and disabled when
using the pep257 and numpy conventions.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Args
        distance: Distance traveled.
        time: Time spent traveling.
    Returns
        Speed as distance divided by time.
    Raises
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