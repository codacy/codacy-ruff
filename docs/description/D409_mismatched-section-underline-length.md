# mismatched-section-underline-length (D409)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for section underlines in docstrings that do not match the length of
the corresponding section header.
## Why is this bad?
This rule enforces a consistent style for multiline numpy-style docstrings,
and helps prevent incorrect syntax in docstrings using reStructuredText.
Multiline numpy-style docstrings are typically composed of a summary line,
followed by a blank line, followed by a series of sections. Each section
has a section header and a section body, and there should be a series of
underline characters in the line following the header. The length of the
underline should exactly match the length of the section header.
This rule enforces a consistent style for multiline numpy-style docstrings
with sections. If your docstring uses reStructuredText, the rule also
helps protect against incorrect reStructuredText syntax, which would cause
errors if you tried to use a tool such as Sphinx to generate documentation
from the docstring.
This rule is enabled when using the numpy convention, and disabled
when using the google or pep257 conventions.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Parameters
    ---
    distance : float
        Distance traveled.
    time : float
        Time spent traveling.
    Returns
    ---
    float
        Speed as distance divided by time.
    Raises
    ---
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