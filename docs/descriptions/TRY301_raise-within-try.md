# raise-within-try (TRY301)
Derived from the tryceratops linter.
## What it does
Checks for raise statements within try blocks. The only raises
caught are those that throw exceptions caught by the try statement itself.
## Why is this bad?
Raising and catching exceptions within the same try block is redundant,
as the code can be refactored to avoid the try block entirely.
Alternatively, the raise can be moved within an inner function, making
the exception reusable across multiple call sites.
## Example
```
def bar():
    pass
def foo():
    try:
        a = bar()
        if not a:
            raise ValueError
    except ValueError:
        raise
```
## Use instead:
```
def bar():
    raise ValueError
def foo():
    try:
        a = bar()  # refactored `bar` to raise `ValueError`
    except ValueError:
        raise
```