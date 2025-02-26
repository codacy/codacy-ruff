# empty-comment (PLR2044)
Derived from the Pylint linter.
Fix is always available.
## What it does
Checks for a # symbol appearing on a line not followed by an actual comment.
## Why is this bad?
Empty comments don't provide any clarity to the code, and just add clutter.
Either add a comment or delete the empty comment.
## Example
```
class Foo:  #
    pass
```
## Use instead:
```
class Foo:
    pass
```