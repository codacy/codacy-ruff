# verbose-decimal-constructor (FURB157)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for unnecessary string literal or float casts in Decimal
constructors.
## Why is this bad?
The Decimal constructor accepts a variety of arguments, including
integers, floats, and strings. However, it's not necessary to cast
integer literals to strings when passing them to the Decimal.
Similarly, Decimal accepts inf, -inf, and nan as string literals,
so there's no need to wrap those values in a float call when passing
them to the Decimal constructor.
Prefer the more concise form of argument passing for Decimal
constructors, as it's more readable and idiomatic.
## Example
```
Decimal("0")
Decimal(float("Infinity"))
```
## Use instead:
```
Decimal(0)
Decimal("Infinity")
```