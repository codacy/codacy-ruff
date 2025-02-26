# missing-new-line-after-section-name (D406)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for section headers in docstrings that are followed by non-newline
characters.
## Why is this bad?
This rule enforces a consistent style for multiline numpy-style docstrings.
Multiline numpy-style docstrings are typically composed of a summary line,
followed by a blank line, followed by a series of sections. Each section
has a section header and a section body. The section header should be
followed by a newline, rather than by some other character (like a colon).
This rule is enabled when using the numpy convention, and disabled
when using the google or pep257 conventions.
## Example
```
# The `Parameters`, `Returns` and `Raises` section headers are all followed
# by a colon in this function's docstring:
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Parameters:
    -----------
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.
    Returns:
    --------
    float
        Speed as distance divided by time.
    Raises:
    -------
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