# if-exp-instead-of-or-operator (FURB110)
Added in 0.15.0 ·
Related issues ·
View source
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for ternary if expressions that can be replaced with the or
operator.
## Why is this bad?
Ternary if expressions are more verbose than or expressions while
providing the same functionality.
## Example
```
x, y = 1, 2
z = x if x else y
```
## Use instead:
```
x, y = 1, 2
z = x or y
Fix safety
This rule's fix is marked as unsafe in the event that the body of the
if expression contains side effects or comments.
For example, foo will be called twice in foo() if foo() else bar()
(assuming foo() returns a truthy value), but only once in
foo() or bar().
```