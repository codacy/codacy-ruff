# return-outside-function (F706)
Derived from the Pyflakes linter.
## What it does
Checks for return statements outside of functions.
## Why is this bad?
The use of a return statement outside of a function will raise a
SyntaxError.
## Example
```
class Foo:
    return 1
```