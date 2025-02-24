# non-augmented-assignment (PLR6104)
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for assignments that can be replaced with augmented assignment
statements.
## Why is this bad?
If the right-hand side of an assignment statement consists of a binary
operation in which one operand is the same as the assignment target,
it can be rewritten as an augmented assignment. For example, x = x + 1
can be rewritten as x += 1.
When performing such an operation, an augmented assignment is more concise
and idiomatic.
Known problems
In some cases, this rule will not detect assignments in which the target
is on the right-hand side of a binary operation (e.g., x = y + x, as
opposed to x = x + y), as such operations are not commutative for
certain data types, like strings.
For example, x = "prefix-" + x is not equivalent to x += "prefix-",
while x = 1 + x is equivalent to x += 1.
If the type of the left-hand side cannot be trivially inferred, the rule
will ignore the assignment.
## Example
```
x = x + 1
```
## Use instead:
```
x += 1
Fix safety
This rule's fix is marked as unsafe, as augmented assignments have
different semantics when the target is a mutable data type, like a list or
dictionary.
For example, consider the following:
foo = [1]
bar = foo
foo = foo + [2]
assert (foo, bar) == ([1, 2], [1])
If the assignment is replaced with an augmented assignment, the update
operation will apply to both foo and bar, as they refer to the same
object:
foo = [1]
bar = foo
foo += [2]
assert (foo, bar) == ([1, 2], [1, 2])
```