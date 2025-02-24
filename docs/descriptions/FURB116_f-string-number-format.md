# f-string-number-format (FURB116)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
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
```