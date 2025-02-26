# forward-annotation-syntax-error (F722)
Derived from the Pyflakes linter.
## What it does
Checks for forward annotations that include invalid syntax.
## Why is this bad?
In Python, type annotations can be quoted as strings literals to enable
references to types that have not yet been defined, known as "forward
references".
However, these quoted annotations must be valid Python expressions. The use
of invalid syntax in a quoted annotation won't raise a SyntaxError, but
will instead raise an error when type checking is performed.
## Example
```
def foo() -> "/": ...
```