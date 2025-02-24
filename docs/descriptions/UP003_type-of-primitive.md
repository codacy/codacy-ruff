# type-of-primitive (UP003)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for uses of type that take a primitive as an argument.
## Why is this bad?
type() returns the type of a given object. A type of a primitive can
always be known in advance and accessed directly, which is more concise
and explicit than using type().
## Example
```
type(1)
```
## Use instead:
```
int
```