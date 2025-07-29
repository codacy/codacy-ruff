# unreliable-callable-check (B004)
Derived from the flake8-bugbear linter.
Fix is sometimes available.
## What it does
Checks for uses of hasattr to test if an object is callable (e.g.,
hasattr(obj, "__call__")).
## Why is this bad?
Using hasattr is an unreliable mechanism for testing if an object is
callable. If obj implements a custom __getattr__, or if its __call__
is itself not callable, you may get misleading results.
Instead, use callable(obj) to test if obj is callable.
## Example
```
hasattr(obj, "__call__")
```
## Use instead:
```
callable(obj)
Fix safety
This rule's fix is marked as unsafe if there's comments in the hasattr call
expression, as comments may be removed.
For example, the fix would be marked as unsafe in the following case:
hasattr(
    # comment 1
    obj,  # comment 2
    # comment 3
    "__call__",  # comment 4
    # comment 5
)
```