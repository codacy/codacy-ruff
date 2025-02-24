# assert-false (B011)
Derived from the flake8-bugbear linter.
Fix is always available.
## What it does
Checks for uses of assert False.
## Why is this bad?
Python removes assert statements when running in optimized mode
(python -O), making assert False an unreliable means of
raising an AssertionError.
Instead, raise an AssertionError directly.
## Example
```
assert False
```
## Use instead:
```
raise AssertionError
Fix safety
This rule's fix is marked as unsafe, as changing an assert to a
raise will change the behavior of your program when running in
optimized mode (python -O).
```