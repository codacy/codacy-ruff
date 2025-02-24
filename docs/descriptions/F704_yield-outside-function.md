# yield-outside-function (F704)
Derived from the Pyflakes linter.
## What it does
Checks for yield, yield from, and await usages outside of functions.
## Why is this bad?
The use of yield, yield from, or await outside of a function will
raise a SyntaxError.
## Example
```
class Foo:
    yield 1
Notebook behavior
As an exception, await is allowed at the top level of a Jupyter notebook
(see: autoawait).
```