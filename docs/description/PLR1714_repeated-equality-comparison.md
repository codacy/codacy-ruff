# repeated-equality-comparison (PLR1714)
Derived from the Pylint linter.
Fix is always available.
## What it does
Checks for repeated equality comparisons that can be rewritten as a membership
test.
This rule will try to determine if the values are hashable
and the fix will use a set if they are. If unable to determine, the fix
will use a tuple and suggest the use of a set.
## Why is this bad?
To check if a variable is equal to one of many values, it is common to
write a series of equality comparisons (e.g.,
foo == "bar" or foo == "baz").
Instead, prefer to combine the values into a collection and use the in
operator to check for membership, which is more performant and succinct.
If the items are hashable, use a set for efficiency; otherwise, use a
tuple.
## Example
```
foo == "bar" or foo == "baz" or foo == "qux"
```
## Use instead:
```
foo in {"bar", "baz", "qux"}
```