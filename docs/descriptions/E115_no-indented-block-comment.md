# no-indented-block-comment (E115)
Derived from the pycodestyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for comments in a code blocks that are lacking indentation.
## Why is this bad?
Comments within an indented block should themselves be indented, to
indicate that they are part of the block.
## Example
```
for item in items:
# Hi
    pass
```
## Use instead:
```
for item in items:
    # Hi
    pass
```