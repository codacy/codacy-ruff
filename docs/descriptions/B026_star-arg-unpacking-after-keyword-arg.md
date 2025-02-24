# star-arg-unpacking-after-keyword-arg (B026)
Derived from the flake8-bugbear linter.
## What it does
Checks for function calls that use star-argument unpacking after providing a
keyword argument
## Why is this bad?
In Python, you can use star-argument unpacking to pass a list or tuple of
arguments to a function.
Providing a star-argument after a keyword argument can lead to confusing
behavior, and is only supported for backwards compatibility.
## Example
```
def foo(x, y, z):
    return x, y, z
foo(1, 2, 3)  # (1, 2, 3)
foo(1, *[2, 3])  # (1, 2, 3)
# foo(x=1, *[2, 3])  # TypeError
# foo(y=2, *[1, 3])  # TypeError
foo(z=3, *[1, 2])  # (1, 2, 3)  # No error, but confusing!
```
## Use instead:
```
def foo(x, y, z):
    return x, y, z
foo(1, 2, 3)  # (1, 2, 3)
foo(x=1, y=2, z=3)  # (1, 2, 3)
foo(*[1, 2, 3])  # (1, 2, 3)
foo(*[1, 2], 3)  # (1, 2, 3)
```