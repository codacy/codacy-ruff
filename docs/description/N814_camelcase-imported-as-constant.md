# camelcase-imported-as-constant (N814)
Derived from the pep8-naming linter.
## What it does
Checks for CamelCase imports that are aliased to constant-style names.
## Why is this bad?
PEP 8 recommends naming conventions for classes, functions,
constants, and more. The use of inconsistent naming styles between
import and alias names may lead readers to expect an import to be of
another type (e.g., confuse a Python class with a constant).
Import aliases should thus follow the same naming style as the member
being imported.
## Example
```
from example import MyClassName as MY_CLASS_NAME
```
## Use instead:
```
from example import MyClassName
Note
Identifiers consisting of a single uppercase character are ambiguous under
the rules of PEP 8, which specifies CamelCase for classes and
ALL_CAPS_SNAKE_CASE for constants. Without a second character, it is not
possible to reliably guess whether the identifier is intended to be part
of a CamelCase string for a class or an ALL_CAPS_SNAKE_CASE string for
a constant, since both conventions will produce the same output when given
a single input character. Therefore, this lint rule does not apply to cases
where the alias for the imported identifier consists of a single uppercase
character.
A common example of a single uppercase character being used for a class
name can be found in Django's django.db.models.Q class.
```