# useless-if-else (RUF034)
Added in 0.9.0 ·
Related issues ·
View source
## What it does
Checks for useless if-else conditions with identical arms.
## Why is this bad?
Useless if-else conditions add unnecessary complexity to the code without
providing any logical benefit. Assigning the value directly is clearer.
## Example
```
foo = x if y else x
```
## Use instead:
```
foo = x
```