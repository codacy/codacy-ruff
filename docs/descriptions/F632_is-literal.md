# is-literal (F632)
Derived from the Pyflakes linter.
Fix is always available.
## What it does
Checks for is and is not comparisons against literals, like integers,
strings, or lists.
## Why is this bad?
The is and is not comparators operate on identity, in that they check
whether two objects are the same object. If the objects are not the same
object, the comparison will always be False. Using is and is not with
constant literals often works "by accident", but are not guaranteed to produce
the expected result.
As of Python 3.8, using is and is not with constant literals will produce
a SyntaxWarning.
This rule will also flag is and is not comparisons against non-constant
literals, like lists, sets, and dictionaries. While such comparisons will
not raise a SyntaxWarning, they are still likely to be incorrect, as they
will compare the identities of the objects instead of their values, which
will always evaluate to False.
Instead, use == and != to compare literals, which will compare the
values of the objects instead of their identities.
## Example
```
x = 200
if x is 200:
    print("It's 200!")
```
## Use instead:
```
x = 200
if x == 200:
    print("It's 200!")
```