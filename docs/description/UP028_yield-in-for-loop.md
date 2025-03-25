# yield-in-for-loop (UP028)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for for loops that can be replaced with yield from expressions.
## Why is this bad?
If a for loop only contains a yield statement, it can be replaced with a
yield from expression, which is more concise and idiomatic.
## Example
```
for x in foo:
    yield x
global y
for y in foo:
    yield y
```
## Use instead:
```
yield from foo
for _element in foo:
    y = _element
    yield y
Fix safety
This rule's fix is marked as unsafe, as converting a for loop to a yield from expression can change the behavior of the program in rare cases.
For example, if a generator is being sent values via send, then rewriting
to a yield from could lead to an attribute error if the underlying
generator does not implement the send method.
Additionally, if at least one target is global or nonlocal,
no fix will be offered.
In most cases, however, the fix is safe, and such a modification should have
no effect on the behavior of the program.
```