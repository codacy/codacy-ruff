# unused-variable (F841)
Added in v0.0.22 ·
Related issues ·
View source
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for the presence of unused variables in function scopes.
## Why is this bad?
A variable that is defined but not used is likely a mistake, and should
be removed to avoid confusion.
If a variable is intentionally defined-but-not-used, it should be
prefixed with an underscore, or some other value that adheres to the
lint.dummy-variable-rgx pattern.
## Example
```
def foo():
    x = 1
    y = 2
    return x
```
## Use instead:
```
def foo():
    x = 1
    return x
Fix safety
This rule's fix is marked as unsafe because removing an unused variable assignment may
delete comments that are attached to the assignment.
See also
This rule does not apply to bindings in unpacked assignments (e.g. x, y = 1, 2). See
unused-unpacked-variable for this case.
```