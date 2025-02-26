# no-blank-line-after-section (D410)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstring sections that are not separated by a single blank
line.
## Why is this bad?
This rule enforces consistency in your docstrings, and helps ensure
compatibility with documentation tooling.
Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body. If a multiline numpy-style or Google-style docstring
consists of multiple sections, each section should be separated by a single
blank line.
This rule is enabled when using the numpy and google conventions, and
disabled when using the pep257 convention.
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