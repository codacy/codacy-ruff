# unnecessary-from-float (FURB164)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for unnecessary from_float and from_decimal usages to construct
Decimal and Fraction instances.
## Why is this bad?
Since Python 3.2, the Fraction and Decimal classes can be constructed
by passing float or decimal instances to the constructor directly. As such,
the use of from_float and from_decimal methods is unnecessary, and
should be avoided in favor of the more concise constructor syntax.
## Examples
```
Decimal.from_float(4.2)
Decimal.from_float(float("inf"))
Fraction.from_float(4.2)
Fraction.from_decimal(Decimal("4.2"))
```
## Use instead:
```
Decimal(4.2)
Decimal("inf")
Fraction(4.2)
Fraction(Decimal(4.2))
```