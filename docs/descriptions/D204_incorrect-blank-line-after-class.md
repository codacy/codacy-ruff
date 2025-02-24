# incorrect-blank-line-after-class (D204)
Derived from the pydocstyle linter.
Fix is always available.
## What it does
Checks for class methods that are not separated from the class's docstring
by a blank line.
## Why is this bad?
PEP 257 recommends the use of a blank line to separate a class's
docstring from its methods.
This rule may not apply to all projects; its applicability is a matter of
convention. By default, this rule is enabled when using the numpy and pep257
conventions, and disabled when using the google convention.
## Example
```
class PhotoMetadata:
    """Metadata about a photo."""
    def __init__(self, file: Path):
        ...
```
## Use instead:
```
class PhotoMetadata:
    """Metadata about a photo."""
    def __init__(self, file: Path):
        ...
```