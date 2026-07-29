# unexpected-indentation-comment (E116)
Preview (since v0.0.269) ·
Related issues ·
View source
Derived from the pycodestyle linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for unexpected indentation of comment.
## Why is this bad?
Comments should match the indentation of the containing code block.
## Example
```
a = 1
    # b = 2
```
## Use instead:
```
a = 1
# b = 2
```