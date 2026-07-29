# complex-structure (C901)
Added in v0.0.127 ·
Related issues ·
View source
Derived from the mccabe linter.
## What it does
Checks for functions with a high McCabe complexity.
## Why is this bad?
The McCabe complexity of a function is a measure of the complexity of
the control flow graph of the function. It is calculated by adding
one to the number of decision points in the function. A decision
point is a place in the code where the program has a choice of two
or more paths to follow.
Functions with a high complexity are hard to understand and maintain.
## Example
```
def normalize_status(status):
    if status == "new":
        return "queued"
    if status == "queued":
        return "running"
    if status == "running":
        return "done"
    if status == "failed":
        return "retry"
    if status == "cancelled":
        return "closed"
    return "unknown"
```
## Use instead:
```
STATUS_TRANSITIONS = {
    "new": "queued",
    "queued": "running",
    "running": "done",
    "failed": "retry",
    "cancelled": "closed",
}
def normalize_status(status):
    return STATUS_TRANSITIONS.get(status, "unknown")
Note that this example assumes a lint.mccabe.max-complexity of 5 or less to trigger a
diagnostic because the initial code only has a complexity of 6.
```