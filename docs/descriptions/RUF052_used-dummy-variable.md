# used-dummy-variable (RUF052)
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for "dummy variables" (variables that are named as if to indicate they are unused)
that are in fact used.
By default, "dummy variables" are any variables with names that start with leading
underscores. However, this is customisable using the lint.dummy-variable-rgx setting).
## Why is this bad?
Marking a variable with a leading underscore conveys that it is intentionally unused within the function or method.
When these variables are later referenced in the code, it causes confusion and potential misunderstandings about
the code's intention. If a variable marked as "unused" is subsequently used, it suggests that either the variable
could be given a clearer name, or that the code is accidentally making use of the wrong variable.
Sometimes leading underscores are used to avoid variables shadowing other variables, Python builtins, or Python
keywords. However, PEP 8 recommends to use trailing underscores for this rather than leading underscores.
Dunder variables are ignored by this rule, as are variables named _.
Only local variables in function scopes are flagged by the rule.
## Example
```
def function():
    _variable = 3
    # important: avoid shadowing the builtin `id()` function!
    _id = 4
    return _variable + _id
```
## Use instead:
```
def function():
    variable = 3
    # important: avoid shadowing the builtin `id()` function!
    id_ = 4
    return variable + id_
Fix availability
The rule's fix is only available for variables that start with leading underscores.
It will also only be available if the "obvious" new name for the variable
would not shadow any other known variables already accessible from the scope
in which the variable is defined.
Fix safety
This rule's fix is marked as unsafe.
For this rule's fix, Ruff renames the variable and fixes up all known references to
it so they point to the renamed variable. However, some renamings also require other
changes such as different arguments to constructor calls or alterations to comments.
Ruff is aware of some of these cases: _T = TypeVar("_T") will be fixed to
T = TypeVar("T") if the _T binding is flagged by this rule. However, in general,
cases like these are hard to detect and hard to automatically fix.
```