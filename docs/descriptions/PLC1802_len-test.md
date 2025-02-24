# len-test (PLC1802)
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for usage of call of 'len' on sequences
in boolean test context.
## Why is this bad?
Empty sequences are considered false in a boolean context.
You can either remove the call to 'len'
or compare the length against a scalar.
## Example
```
fruits = ["orange", "apple"]
vegetables = []
if len(fruits):
    print(fruits)
if not len(vegetables):
    print(vegetables)
```
## Use instead:
```
fruits = ["orange", "apple"]
if fruits:
    print(fruits)
if not vegetables:
    print(vegetables)
```