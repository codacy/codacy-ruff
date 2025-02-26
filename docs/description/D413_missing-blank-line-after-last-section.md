# missing-blank-line-after-last-section (D413)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for missing blank lines after the last section of a multiline
docstring.
## Why is this bad?
This rule enforces a consistent style for multiline docstrings.
Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, the rule is disabled when using the google,
numpy, and pep257 conventions.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Parameters
    ----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.
    Returns
    -------
    float
        Speed as distance divided by time.
    Raises
    ------
    FasterThanLightError
        If speed is greater than the speed of light.
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
    Parameters
    ----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.
    Returns
    -------
    float
        Speed as distance divided by time.
    Raises
    ------
    FasterThanLightError
        If speed is greater than the speed of light.
    """
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
```