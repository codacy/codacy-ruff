# potential-index-error (PLE0643)
Derived from the Pylint linter.
## What it does
Checks for hard-coded sequence accesses that are known to be out of bounds.
## Why is this bad?
Attempting to access a sequence with an out-of-bounds index will cause an
IndexError to be raised at runtime. When the sequence and index are
defined statically (e.g., subscripts on list and tuple literals, with
integer indexes), such errors can be detected ahead of time.
## Example
```
print([0, 1, 2][3])
```