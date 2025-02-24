# single-item-membership-test (FURB171)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for membership tests against single-item containers.
## Why is this bad?
Performing a membership test against a container (like a list or set)
with a single item is less readable and less efficient than comparing
against the item directly.
## Example
```
1 in [1]
```
## Use instead:
```
1 == 1
Fix safety
When the right-hand side is a string, the fix is marked as unsafe.
This is because c in "a" is true both when c is "a" and when c is the empty string,
so the fix can change the behavior of your program in these cases.
Additionally, if there are comments within the fix's range,
it will also be marked as unsafe.
```