# line-contains-fixme (FIX001)
Derived from the flake8-fixme linter.
## What it does
Checks for "FIXME" comments.
## Why is this bad?
"FIXME" comments are used to describe an issue that should be resolved
(usually, a bug or unexpected behavior).
Consider resolving the issue before deploying the code.
Note that if you use "FIXME" comments as a form of documentation, this
rule may not be appropriate for your project.
## Example
```
def speed(distance, time):
    return distance / time  # FIXME: Raises ZeroDivisionError for time = 0.
```