# unnecessary-enumerate (FURB148)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of enumerate that discard either the index or the value
when iterating over a sequence.
## Why is this bad?
The built-in enumerate function is useful when you need both the index and
value of a sequence.
If you only need the index or values of a sequence, you should iterate over
range(len(...)) or the sequence itself, respectively, instead. This is
more efficient and communicates the intent of the code more clearly.
Known problems
This rule is prone to false negatives due to type inference limitations;
namely, it will only suggest a fix using the len builtin function if the
sequence passed to enumerate is an instantiated as a list, set, dict, or
tuple literal, or annotated as such with a type annotation.
The len builtin function is not defined for all object types (such as
generators), and so refactoring to use len over enumerate is not always
safe.
## Example
```
for index, _ in enumerate(sequence):
    print(index)
for _, value in enumerate(sequence):
    print(value)
```
## Use instead:
```
for index in range(len(sequence)):
    print(index)
for value in sequence:
    print(value)
```