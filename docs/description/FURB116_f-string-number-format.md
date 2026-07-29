# f-string-number-format (FURB116)
Added in 0.13.0 ·
Related issues ·
View source
Derived from the refurb linter.
Fix is sometimes available.
## What it does
Checks for uses of bin(...)[2:] (or hex, or oct) to convert
an integer into a string.
## Why is this bad?
When converting an integer to a baseless binary, hexadecimal, or octal
string, using f-strings is more concise and readable than using the
bin, hex, or oct functions followed by a slice.
## Example
```
print(bin(1337)[2:])
```
## Use instead:
```
print(f"{1337:b}")
Fix safety
The fix is only marked as safe for integer literals, all other cases
are display-only, as they may change the runtime behavior of the program
or introduce syntax errors. The fix for integer literals is also marked as unsafe
if the expression contains comments that would be removed by the fix.
```