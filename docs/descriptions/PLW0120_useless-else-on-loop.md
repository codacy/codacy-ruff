# useless-else-on-loop (PLW0120)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for else clauses on loops without a break statement.
## Why is this bad?
When a loop includes an else statement, the code inside the else clause
will be executed if the loop terminates "normally" (i.e., without a
break).
If a loop always terminates "normally" (i.e., does not contain a
break), then the else clause is redundant, as the code inside the
else clause will always be executed.
In such cases, the code inside the else clause can be moved outside the
loop entirely, and the else clause can be removed.
## Example
```
for item in items:
    print(item)
else:
    print("All items printed")
```
## Use instead:
```
for item in items:
    print(item)
print("All items printed")
```