# print (T201)
Derived from the flake8-print linter.
Fix is sometimes available.
## What it does
Checks for print statements.
## Why is this bad?
print statements are useful in some situations (e.g., debugging), but
should typically be omitted from production code. print statements can
lead to the accidental inclusion of sensitive information in logs, and are
not configurable by clients, unlike logging statements.
## Example
```
def add_numbers(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
    return a + b
```
## Use instead:
```
def add_numbers(a, b):
    return a + b
Fix safety
This rule's fix is marked as unsafe, as it may remove print statements
that are used beyond debugging purposes.
```