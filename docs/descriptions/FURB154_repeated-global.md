# repeated-global (FURB154)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for consecutive global (or nonlocal) statements.
## Why is this bad?
The global and nonlocal keywords accepts multiple comma-separated names.
Instead of using multiple global (or nonlocal) statements for separate
variables, you can use a single statement to declare multiple variables at
once.
## Example
```
def func():
    global x
    global y
    print(x, y)
```
## Use instead:
```
def func():
    global x, y
    print(x, y)
```