# non-pep695-generic-function (UP047)
Derived from the pyupgrade linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for use of standalone type variables and parameter specifications in generic functions.
## Why is this bad?
Special type parameter syntax was introduced in Python 3.12 by PEP 695 for defining generic
functions. This syntax is easier to read and provides cleaner support for generics.
Known problems
The rule currently skips generic functions nested inside of other functions or classes and those
with type parameters containing the default argument introduced in PEP 696 and implemented
in Python 3.13.
Not all type checkers fully support PEP 695 yet, so even valid fixes suggested by this rule may
cause type checking to fail.
Fix safety
This fix is marked unsafe, as PEP 695 uses inferred variance for type parameters, instead of
the covariant and contravariant keywords used by TypeVar variables. As such, replacing a
TypeVar variable with an inline type parameter may change its variance.
Additionally, if the rule cannot determine whether a parameter annotation corresponds to a type
variable (e.g. for a type imported from another module), it will not add the type to the generic
type parameter list. This causes the function to have a mix of old-style type variables and
new-style generic type parameters, which will be rejected by type checkers.
## Example
```
from typing import TypeVar
T = TypeVar("T")
def generic_function(var: T) -> T:
    return var
```
## Use instead:
```
def generic_function[T](var: T) -> T:
    return var
See also
This rule replaces standalone type variables in function signatures but doesn't remove
the corresponding type variables even if they are unused after the fix. See
unused-private-type-var for a rule to clean up unused
private type variables.
This rule will not rename private type variables to remove leading underscores, even though the
new type parameters are restricted in scope to their associated function. See
private-type-parameter for a rule to update these names.
This rule only applies to generic functions and does not include generic classes. See
non-pep695-generic-class for the class version.
```