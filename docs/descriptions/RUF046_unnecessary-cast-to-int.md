# unnecessary-cast-to-int (RUF046)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for int conversions of values that are already integers.
## Why is this bad?
Such a conversion is unnecessary.
Known problems
This rule may produce false positives for round, math.ceil, math.floor,
and math.trunc calls when values override the __round__, __ceil__, __floor__,
or __trunc__ operators such that they don't return an integer.
## Example
```
int(len([]))
int(round(foo, None))
```
## Use instead:
```
len([])
round(foo)
Fix safety
The fix for round, math.ceil, math.floor, and math.truncate is unsafe
because removing the int conversion can change the semantics for values
overriding the __round__, __ceil__, __floor__, or __trunc__ dunder methods
such that they don't return an integer.
```