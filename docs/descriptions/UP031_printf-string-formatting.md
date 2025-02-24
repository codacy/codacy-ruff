# printf-string-formatting (UP031)
Derived from the pyupgrade linter.
Fix is sometimes available.
## What it does
Checks for printf-style string formatting, and offers to replace it with
str.format calls.
## Why is this bad?
printf-style string formatting has a number of quirks, and leads to less
readable code than using str.format calls or f-strings. In general, prefer
the newer str.format and f-strings constructs over printf-style string
formatting.
## Example
```
"%s, %s" % ("Hello", "World")  # "Hello, World"
```
## Use instead:
```
"{}, {}".format("Hello", "World")  # "Hello, World"
f"{'Hello'}, {'World'}"  # "Hello, World"
Fix safety
In cases where the format string contains a single generic format specifier
(e.g. %s), and the right-hand side is an ambiguous expression,
we cannot offer a safe fix.
For example, given:
"%s" % val
val could be a single-element tuple, or a single value (not
contained in a tuple). Both of these would resolve to the same
formatted string when using printf-style formatting, but
resolve differently when using f-strings:
val = 1
print("%s" % val)  # "1"
print("{}".format(val))  # "1"
val = (1,)
print("%s" % val)  # "1"
print("{}".format(val))  # "(1,)"
```