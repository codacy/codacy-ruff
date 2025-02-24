# if-exp-instead-of-or-operator (FURB110)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for ternary if expressions that can be replaced with the or
operator.
## Why is this bad?
Ternary if expressions are more verbose than or expressions while
providing the same functionality.
## Example
```
z = x if x else y
```
## Use instead:
```
z = x or y
Fix safety
This rule's fix is marked as unsafe in the event that the body of the
if expression contains side effects.
For example, foo will be called twice in foo() if foo() else bar()
(assuming foo() returns a truthy value), but only once in
foo() or bar().
```