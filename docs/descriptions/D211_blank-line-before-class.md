# blank-line-before-class (D211)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstrings on class definitions that are preceded by a blank
line.
## Why is this bad?
Avoid introducing any blank lines between a class definition and its
docstring, for consistency.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the google,
numpy, and pep257 conventions.
For an alternative, see D203.
## Example
```
class PhotoMetadata:
    """Metadata about a photo."""
```
## Use instead:
```
class PhotoMetadata:
    """Metadata about a photo."""
```