# incorrect-blank-line-before-class (D203)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for docstrings on class definitions that are not preceded by a
blank line.
## Why is this bad?
Use a blank line to separate the docstring from the class definition, for
consistency.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is disabled when using the google,
numpy, and pep257 conventions.
For an alternative, see D211.
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