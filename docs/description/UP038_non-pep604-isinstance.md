# non-pep604-isinstance (UP038)
Derived from the pyupgrade linter.
Warning: This rule is deprecated and will be removed in a future release.
Fix is always available.
Deprecation
This rule was deprecated as using PEP 604 syntax in isinstance and issubclass calls
isn't recommended practice, and it incorrectly suggests that other typing syntaxes like PEP 695
would be supported by isinstance and issubclass. Using the PEP 604 syntax
is also slightly slower.
## What it does
Checks for uses of isinstance and issubclass that take a tuple
of types for comparison.
## Why is this bad?
Since Python 3.10, isinstance and issubclass can be passed a
|-separated union of types, which is consistent
with the union operator introduced in PEP 604.
Note that this results in slower code. Ignore this rule if the
performance of an isinstance or issubclass check is a
concern, e.g., in a hot loop.
## Example
```
isinstance(x, (int, float))
```
## Use instead:
```
isinstance(x, int | float)
```