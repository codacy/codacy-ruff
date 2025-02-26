# redefined-loop-name (PLW2901)
Derived from the Pylint linter.
## What it does
Checks for variables defined in for loops and with statements that
get overwritten within the body, for example by another for loop or
with statement or by direct assignment.
## Why is this bad?
Redefinition of a loop variable inside the loop's body causes its value
to differ from the original loop iteration for the remainder of the
block, in a way that will likely cause bugs.
In Python, unlike many other languages, for loops and with
statements don't define their own scopes. Therefore, a nested loop that
uses the same target variable name as an outer loop will reuse the same
actual variable, and the value from the last iteration will "leak out"
into the remainder of the enclosing loop.
While this mistake is easy to spot in small examples, it can be hidden
in larger blocks of code, where the definition and redefinition of the
variable may not be visible at the same time.
## Example
```
for i in range(10):
    i = 9
    print(i)  # prints 9 every iteration
for i in range(10):
    for i in range(10):  # original value overwritten
        pass
    print(i)  # also prints 9 every iteration
with path1.open() as f:
    with path2.open() as f:
        f = path2.open()
    print(f.readline())  # prints a line from path2
```