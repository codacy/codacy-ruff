# unnecessary-placeholder (PIE790)
Derived from the flake8-pie linter.
Fix is always available.
## What it does
Checks for unnecessary pass statements and ellipsis (...) literals in
functions, classes, and other blocks.
## Why is this bad?
In Python, the pass statement and ellipsis (...) literal serve as
placeholders, allowing for syntactically correct empty code blocks. The
primary purpose of these nodes is to avoid syntax errors in situations
where a statement or expression is syntactically required, but no code
needs to be executed.
If a pass or ellipsis is present in a code block that includes at least
one other statement (even, e.g., a docstring), it is unnecessary and should
be removed.
## Example
```
def func():
    """Placeholder docstring."""
    pass
```
## Use instead:
```
def func():
    """Placeholder docstring."""
Or, given:
def func():
    """Placeholder docstring."""
    ...
```
## Use instead:
```
def func():
    """Placeholder docstring."""
Fix safety
This rule's fix is marked as unsafe in the rare case that the pass or ellipsis
is followed by a string literal, since removal of the placeholder would convert the
subsequent string literal into a docstring.
```