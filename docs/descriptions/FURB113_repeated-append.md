# repeated-append (FURB113)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for consecutive calls to append.
## Why is this bad?
Consecutive calls to append can be less efficient than batching them into
a single extend. Each append resizes the list individually, whereas an
extend can resize the list once for all elements.
Known problems
This rule is prone to false negatives due to type inference limitations,
as it will only detect lists that are instantiated as literals or annotated
with a type annotation.
## Example
```
nums = [1, 2, 3]
nums.append(4)
nums.append(5)
nums.append(6)
```
## Use instead:
```
nums = [1, 2, 3]
nums.extend((4, 5, 6))
```