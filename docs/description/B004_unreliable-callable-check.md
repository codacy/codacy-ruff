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
```