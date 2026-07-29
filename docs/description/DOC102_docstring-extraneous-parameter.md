# docstring-extraneous-parameter (DOC102)
Preview (since 0.14.1) ·
Related issues ·
View source
Derived from the pydoclint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for function docstrings that include parameters which are not
in the function signature.
## Why is this bad?
If a docstring documents a parameter which is not in the function signature,
it can be misleading to users and/or a sign of incomplete documentation or
refactors.
## Example
```
def calculate_speed(distance: float, time: float) -> float:
    """Calculate speed as distance divided by time.
    Args:
        distance: Distance traveled.
        time: Time spent traveling.
        acceleration: Rate of change of speed.
    Returns:
        Speed as distance divided by time.
    """
    return distance / time
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
    """
    return distance / time
```