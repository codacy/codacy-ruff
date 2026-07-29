# lambda-assignment (E731)
Added in v0.0.28 ·
Related issues ·
View source
Derived from the pycodestyle linter.
Fix is sometimes available.
## What it does
Checks for lambda expressions which are assigned to a variable.
## Why is this bad?
Per PEP 8, you should "Always use a def statement instead of an assignment
statement that binds a lambda expression directly to an identifier."
Using a def statement leads to better tracebacks, and the assignment
itself negates the primary benefit of using a lambda expression (i.e.,
that it can be embedded inside another expression).
## Example
```
f = lambda x: 2 * x
```
## Use instead:
```
def f(x):
    return 2 * x
Fix safety
This fix is marked as unsafe because converting a lambda assignment into a
function definition changes observable properties of the callable.
In particular, a lambda function has the name "<lambda>", while the
generated function uses the name of the assigned variable. Code that relies
on function metadata, such as logging, registration, or introspection, may
therefore behave differently after the fix.
```