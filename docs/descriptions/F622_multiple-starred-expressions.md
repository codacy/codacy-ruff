# multiple-starred-expressions (F622)
Derived from the Pyflakes linter.
## What it does
Checks for the use of multiple starred expressions in assignment statements.
## Why is this bad?
In assignment statements, starred expressions can be used to unpack iterables.
Including more than one starred expression on the left-hand-side of an
assignment will cause a SyntaxError, as it is unclear which expression
should receive the remaining values.
## Example
```
*foo, *bar, baz = (1, 2, 3)
```