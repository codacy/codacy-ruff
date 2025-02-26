# expressions-in-star-assignment (F621)
Derived from the Pyflakes linter.
## What it does
Checks for the use of too many expressions in starred assignment statements.
## Why is this bad?
In assignment statements, starred expressions can be used to unpack iterables.
In Python 3, no more than 1 \<< 8 assignments are allowed before a starred
expression, and no more than 1 \<< 24 expressions are allowed after a starred
expression.
```