# collapsible-else-if (PLR5501)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for else blocks that consist of a single if statement.
## Why is this bad?
If an else block contains a single if statement, it can be collapsed
into an elif, thus reducing the indentation level.
## Example
```
def check_sign(value: int) -> None:
    if value > 0:
        print("Number is positive.")
    else:
        if value < 0:
            print("Number is negative.")
        else:
            print("Number is zero.")
```
## Use instead:
```
def check_sign(value: int) -> None:
    if value > 0:
        print("Number is positive.")
    elif value < 0:
        print("Number is negative.")
    else:
        print("Number is zero.")
```