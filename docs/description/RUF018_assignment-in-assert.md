# assignment-in-assert (RUF018)
## What it does
Checks for named assignment expressions (e.g., x := 0) in assert
statements.
## Why is this bad?
Named assignment expressions (also known as "walrus operators") are used to
assign a value to a variable as part of a larger expression.
Named assignments are syntactically valid in assert statements. However,
when the Python interpreter is run under the -O flag, assert statements
are not executed. In this case, the named assignment will also be ignored,
which may result in unexpected behavior (e.g., undefined variable
accesses).
## Example
```
assert (x := 0) == 0
print(x)
```
## Use instead:
```
x = 0
assert x == 0
print(x)
The rule avoids flagging named expressions that define variables which are
only referenced from inside assert statements; the following will not
trigger the rule:
assert (x := y**2) > 42, f"Expected >42 but got {x}"
Nor will this:
assert (x := y**2) > 42
assert x < 1_000_000
```