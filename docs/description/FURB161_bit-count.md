# bit-count (FURB161)
Derived from the refurb linter.
Fix is always available.
## What it does
Checks for uses of bin(...).count("1") to perform a population count.
## Why is this bad?
In Python 3.10, a bit_count() method was added to the int class,
which is more concise and efficient than converting to a binary
representation via bin(...).
## Example
```
x = bin(123).count("1")
y = bin(0b1111011).count("1")
```
## Use instead:
```
x = (123).bit_count()
y = 0b1111011.bit_count()
```