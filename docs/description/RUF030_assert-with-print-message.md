# assert-with-print-message (RUF030)
Fix is always available.
## What it does
Checks for uses of assert expression, print(message).
## Why is this bad?
If an assert x, y assertion fails, the Python interpreter raises an
AssertionError, and the evaluated value of y is used as the contents of
that assertion error. The print function always returns None, however,
so the evaluated value of a call to print will always be None.
Using a print call in this context will therefore output the message to
stdout, before raising an empty AssertionError(None). Instead, remove
the print and pass the message directly as the second expression,
allowing stderr to capture the message in a well-formatted context.
## Example
```
assert False, print("This is a message")
```
## Use instead:
```
assert False, "This is a message"
Fix safety
This rule's fix is marked as unsafe, as changing the second expression
will result in a different AssertionError message being raised, as well as
a change in stdout output.
```