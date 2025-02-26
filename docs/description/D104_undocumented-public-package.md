# undocumented-public-package (D104)
Derived from the pydocstyle linter.
## What it does
Checks for undocumented public package definitions.
## Why is this bad?
Public packages should be documented via docstrings to outline their
purpose and contents.
Generally, package docstrings should list the modules and subpackages that
are exported by the package.
If the codebase adheres to a standard format for package docstrings, follow
that format for consistency.
## Example
```
__all__ = ["Player", "Game"]
```
## Use instead:
```
"""Game and player management package.
This package provides classes for managing players and games.
"""
__all__ = ["player", "game"]
```