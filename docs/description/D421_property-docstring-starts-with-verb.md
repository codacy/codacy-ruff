# property-docstring-starts-with-verb (D421)
Preview (since 0.15.18) ·
Related issues ·
View source
Derived from the pydocstyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for @property method docstrings that start with known verbs
(e.g., "returns", "gets", etc).
## Why is this bad?
The Google Python style guide recommends that the docstring for a
@property data descriptor use the same style as the docstring for an
attribute or a function argument (e.g., """The Bigtable path."""),
rather than a function-style docstring (e.g.,
"""Returns the Bigtable path.""").
## Example
```
class Foo:
    @property
    def bar(self) -> str:
        """Returns the bar."""
        return self._bar
```
## Use instead:
```
class Foo:
    @property
    def bar(self) -> str:
        """The bar."""
        return self._bar
```