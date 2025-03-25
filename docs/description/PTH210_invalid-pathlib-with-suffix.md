# invalid-pathlib-with-suffix (PTH210)
Derived from the flake8-use-pathlib linter.
Fix is sometimes available.
## What it does
Checks for pathlib.Path.with_suffix() calls where
the given suffix does not have a leading dot
or the given suffix is a single dot ".".
## Why is this bad?
Path.with_suffix() will raise an error at runtime
if the given suffix is not prefixed with a dot
or it is a single dot ".".
## Example
```
path.with_suffix("py")
```
## Use instead:
```
path.with_suffix(".py")
Known problems
This rule is likely to have false negatives, as Ruff can only emit the
lint if it can say for sure that a binding refers to a Path object at
runtime. Due to type inference limitations, Ruff is currently only
confident about this if it can see that the binding originates from a
function parameter annotated with Path or from a direct assignment to a
Path() constructor call.
Fix safety
The fix for this rule adds a leading period to the string passed
to the with_suffix() call. This fix is marked as unsafe, as it
changes runtime behaviour: the call would previously always have
raised an exception, but no longer will.
Moreover, it's impossible to determine if this is the correct fix
for a given situation (it's possible that the string was correct
but was being passed to the wrong method entirely, for example).
No fix is offered if the suffix "." is given, since the intent is unclear.
```