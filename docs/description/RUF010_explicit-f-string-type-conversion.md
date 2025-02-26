# explicit-f-string-type-conversion (RUF010)
Fix is always available.
## What it does
Checks for uses of str(), repr(), and ascii() as explicit type
conversions within f-strings.
## Why is this bad?
f-strings support dedicated conversion flags for these types, which are
more succinct and idiomatic.
Note that, in many cases, calling str() within an f-string is
unnecessary and can be removed entirely, as the value will be converted
to a string automatically, the notable exception being for classes that
implement a custom __format__ method.
## Example
```
a = "some string"
f"{repr(a)}"
```
## Use instead:
```
a = "some string"
f"{a!r}"
```