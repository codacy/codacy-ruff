# type-check-without-type-error (TRY004)
Added in v0.0.230 ·
Related issues ·
View source
Derived from the tryceratops linter.
## What it does
Checks for type checks that do not raise TypeError.
## Why is this bad?
The Python documentation states that TypeError should be raised upon
encountering an inappropriate type.
## Example
```
def foo(n: int):
    if isinstance(n, int):
        pass
    else:
        raise ValueError("n must be an integer")
```
## Use instead:
```
def foo(n: int):
    if isinstance(n, int):
        pass
    else:
        raise TypeError("n must be an integer")
```