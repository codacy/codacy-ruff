# enumerate-for-loop (SIM113)
Derived from the flake8-simplify linter.
## What it does
Checks for for loops with explicit loop-index variables that can be replaced
with enumerate().
## Why is this bad?
When iterating over a sequence, it's often desirable to keep track of the
index of each element alongside the element itself. Prefer the enumerate
builtin over manually incrementing a counter variable within the loop, as
enumerate is more concise and idiomatic.
## Example
```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"{i + 1}. {fruit}")
    i += 1
```
## Use instead:
```
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i + 1}. {fruit}")
```