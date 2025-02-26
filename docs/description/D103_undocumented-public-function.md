# undocumented-public-function (D103)
Derived from the pydocstyle linter.
## What it does
Checks for undocumented public function definitions.
## Why is this bad?
Public functions should be documented via docstrings to outline their
purpose and behavior.
Generally, a function docstring should describe the function's behavior,
arguments, side effects, exceptions, return values, and any other
information that may be relevant to the user.
If the codebase adheres to a standard format for function docstrings, follow
that format for consistency.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    try:
        return distance / time
    except ZeroDivisionError as exc:
        raise FasterThanLightError from exc
Use instead (using the NumPy docstring format):
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
Or, using the Google docstring format:
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