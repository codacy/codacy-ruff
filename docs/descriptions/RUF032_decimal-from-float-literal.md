# decimal-from-float-literal (RUF032)
Fix is always available.
## What it does
Checks for Decimal calls passing a float literal.
## Why is this bad?
Float literals have limited precision that can lead to unexpected results.
The Decimal class is designed to handle numbers with fixed-point precision,
so a string literal should be used instead.
## Example
```
num = Decimal(1.2345)
```
## Use instead:
```
num = Decimal("1.2345")
Fix Safety
This rule's fix is marked as unsafe because it changes the underlying value
of the Decimal instance that is constructed. This can lead to unexpected
behavior if your program relies on the previous value (whether deliberately or not).
```