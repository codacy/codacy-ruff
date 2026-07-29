# unnecessary-assign-before-yield (RUF070)
Preview (since 0.15.3) ·
Related issues ·
View source
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for variable assignments that immediately precede a yield (or
yield from) of the assigned variable, where the variable is not
referenced anywhere else.
## Why is this bad?
The variable assignment is not necessary, as the value can be yielded
directly.
## Example
```
def gen():
    x = 1
    yield x
```
## Use instead:
```
def gen():
    yield 1
Fix safety
This fix is always marked as unsafe because removing the intermediate
variable assignment changes the local variable bindings visible to
locals() and debuggers when the generator is suspended at the yield.
```