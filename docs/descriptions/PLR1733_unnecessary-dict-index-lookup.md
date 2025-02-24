# unnecessary-dict-index-lookup (PLR1733)
Derived from the Pylint linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for key-based dict accesses during .items() iterations.
## Why is this bad?
When iterating over a dict via .items(), the current value is already
available alongside its key. Using the key to look up the value is
unnecessary.
## Example
```
FRUITS = {"apple": 1, "orange": 10, "berry": 22}
for fruit_name, fruit_count in FRUITS.items():
    print(FRUITS[fruit_name])
```
## Use instead:
```
FRUITS = {"apple": 1, "orange": 10, "berry": 22}
for fruit_name, fruit_count in FRUITS.items():
    print(fruit_count)
```