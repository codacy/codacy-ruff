# undocumented-param (D417)
Derived from the pydocstyle linter.
## What it does
Checks for function docstrings that do not include documentation for all
parameters in the function.
## Why is this bad?
This rule helps prevent you from leaving Google-style docstrings unfinished
or incomplete. Multiline Google-style docstrings should describe all
parameters for the function they are documenting.
Multiline docstrings are typically composed of a summary line, followed by
a blank line, followed by a series of sections, each with a section header
and a section body. Function docstrings often include a section for
function arguments; this rule is concerned with that section only.
Note that this rule only checks docstrings with an arguments (e.g. Args) section.
This rule is enabled when using the google convention, and disabled when
using the pep257 and numpy conventions.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Args:
        distance: Distance traveled.
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