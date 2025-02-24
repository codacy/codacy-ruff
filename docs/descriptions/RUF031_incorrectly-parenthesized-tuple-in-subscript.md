# incorrectly-parenthesized-tuple-in-subscript (RUF031)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for consistent style regarding whether nonempty tuples in subscripts
are parenthesized.
The exact nature of this violation depends on the setting
lint.ruff.parenthesize-tuple-in-subscript. By default, the use of
parentheses is considered a violation.
This rule is not applied inside "typing contexts" (type annotations,
type aliases and subscripted class bases), as these have their own specific
conventions around them.
## Why is this bad?
It is good to be consistent and, depending on the codebase, one or the other
convention may be preferred.
## Example
```
directions = {(0, 1): "North", (1, 0): "East", (0, -1): "South", (-1, 0): "West"}
directions[(0, 1)]
Use instead (with default setting):
directions = {(0, 1): "North", (1, 0): "East", (0, -1): "South", (-1, 0): "West"}
directions[0, 1]
```