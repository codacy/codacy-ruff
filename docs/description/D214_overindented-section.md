# overindented-section (D214)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for over-indented sections in docstrings.
## Why is this bad?
This rule enforces a consistent style for docstrings with multiple
sections.
Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body. The convention is that all sections should use
consistent indentation. In each section, the header should match the
indentation of the docstring's opening quotes, and the body should be
indented one level further.
This rule is enabled when using the numpy and google conventions, and
disabled when using the pep257 convention.
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