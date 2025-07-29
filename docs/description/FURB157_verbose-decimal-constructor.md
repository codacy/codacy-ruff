# verbose-decimal-constructor (FURB157)
Derived from the refurb linter.
Fix is always available.
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
Note that this rule does not flag quoted float literals such as Decimal("0.1"), which will
produce a more precise Decimal value than the unquoted Decimal(0.1).
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