# private-type-parameter (UP049)
Derived from the pyupgrade linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for use of PEP 695 type parameters with leading underscores in generic classes and
functions.
## Why is this bad?
PEP 695 type parameters are already restricted in scope to the class or function in which they
appear, so leading underscores just hurt readability without the usual privacy benefits.
However, neither a diagnostic nor a fix will be emitted for "sunder" (_T_) or "dunder"
(__T__) type parameter names as these are not considered private.
## Example
```
class GenericClass[_T]:
    var: _T
def generic_function[_T](var: _T) -> list[_T]:
    return var[0]
```
## Use instead:
```
class GenericClass[T]:
    var: T
def generic_function[T](var: T) -> list[T]:
    return var[0]
Fix availability
If the name without an underscore would shadow a builtin or another variable, would be a
keyword, or would otherwise be an invalid identifier, a fix will not be available. In these
situations, you can consider using a trailing underscore or a different name entirely to satisfy
the lint rule.
See also
This rule renames private PEP 695 type parameters but doesn't convert pre-PEP 695 generics
to the new format. See non-pep695-generic-function and
non-pep695-generic-class for rules that will make this transformation.
Those rules do not remove unused type variables after their changes,
so you may also want to consider enabling unused-private-type-var to complete
the transition to PEP 695 generics.
```