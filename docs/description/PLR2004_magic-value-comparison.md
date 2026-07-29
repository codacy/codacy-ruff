# magic-value-comparison (PLR2004)
Added in v0.0.221 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for the use of unnamed numerical constants ("magic") values in
comparisons.
## Why is this bad?
The use of "magic" values can make code harder to read and maintain, as
readers will have to infer the meaning of the value from the context.
Such values are discouraged by PEP 8.
For convenience, this rule excludes a variety of common values from the
"magic" value definition, such as 0, 1, "", and "__main__". It
also exempts comparisons against sys.version, sys.version_info, and
sys.implementation.version.
## Example
```
def apply_discount(price: float) -> float:
    if price <= 100:
        return price / 2
    else:
        return price
```
## Use instead:
```
MAX_DISCOUNT = 100
def apply_discount(price: float) -> float:
    if price <= MAX_DISCOUNT:
        return price / 2
    else:
        return price
```