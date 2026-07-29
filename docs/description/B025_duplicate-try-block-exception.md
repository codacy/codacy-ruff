# duplicate-try-block-exception (B025)
Added in v0.0.67 ·
Related issues ·
View source
Derived from the flake8-bugbear linter.
## What it does
Checks for try-except blocks with duplicate exception handlers.
## Why is this bad?
Duplicate exception handlers are redundant, as the first handler will catch
the exception, making the second handler unreachable.
## Example
```
try:
    ...
except ValueError:
    ...
except ValueError:
    ...
```
## Use instead:
```
try:
    ...
except ValueError:
    ...
Fix safety
This rule's fix is marked as safe, unless the exception handler contains comments.
```