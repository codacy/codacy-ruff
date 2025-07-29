# static-join-to-f-string (FLY002)
Derived from the flynt linter.
Fix is always available.
## What it does
Checks for str.join calls that can be replaced with f-strings.
## Why is this bad?
f-strings are more readable and generally preferred over str.join calls.
## Example
```
" ".join((foo, bar))
```
## Use instead:
```
f"{foo} {bar}"
Fix safety
The fix is always marked unsafe because the evaluation of the f-string
expressions will default to calling the __format__ method of each
object, whereas str.join expects each object to be an instance of
str and uses the corresponding string. Therefore it is possible for
the values of the resulting strings to differ, or for one expression
to raise an exception while the other does not.
```