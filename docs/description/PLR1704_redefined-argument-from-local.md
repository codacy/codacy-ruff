# redefined-argument-from-local (PLR1704)
Derived from the Pylint linter.
## What it does
Checks for variables defined in for, try, with statements
that redefine function parameters.
## Why is this bad?
Redefined variables can cause unexpected behavior because of overridden function parameters.
If nested functions are declared, an inner function's body can override an outer function's parameters.
## Example
```
def show(host_id=10.11):
    for host_id, host in [[12.13, "Venus"], [14.15, "Mars"]]:
        print(host_id, host)
```
## Use instead:
```
def show(host_id=10.11):
    for inner_host_id, host in [[12.13, "Venus"], [14.15, "Mars"]]:
        print(host_id, inner_host_id, host)
```