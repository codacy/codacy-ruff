# undocumented-public-module (D100)
Derived from the pydocstyle linter.
## What it does
Checks for undocumented public module definitions.
## Why is this bad?
Public modules should be documented via docstrings to outline their purpose
and contents.
Generally, module docstrings should describe the purpose of the module and
list the classes, exceptions, functions, and other objects that are exported
by the module, alongside a one-line summary of each.
If the module is a script, the docstring should be usable as its "usage"
message.
If the codebase adheres to a standard format for module docstrings, follow
that format for consistency.
## Example
```
class FasterThanLightError(ZeroDivisionError): ...
def calculate_speed(distance: float, time: float) -> float: ...
```
## Use instead:
```
"""Utility functions and classes for calculating speed.
This module provides:
- FasterThanLightError: exception when FTL speed is calculated;
- calculate_speed: calculate speed given distance and time.
"""
class FasterThanLightError(ZeroDivisionError): ...
def calculate_speed(distance: float, time: float) -> float: ...
Notebook behavior
This rule is ignored for Jupyter Notebooks.
```