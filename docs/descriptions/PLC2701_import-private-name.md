# import-private-name (PLC2701)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for import statements that import a private name (a name starting
with an underscore _) from another module.
## Why is this bad?
PEP 8 states that names starting with an underscore are private. Thus,
they are not intended to be used outside of the module in which they are
defined.
Further, as private imports are not considered part of the public API, they
are prone to unexpected changes, especially outside of semantic versioning.
Instead, consider using the public API of the module.
This rule ignores private name imports that are exclusively used in type
annotations. Ideally, types would be public; however, this is not always
possible when using third-party libraries.
Known problems
Does not ignore private name imports from within the module that defines
the private name if the module is defined with PEP 420 namespace packages
(i.e., directories that omit the __init__.py file). Namespace packages
must be configured via the namespace-packages setting.
## Example
```
from foo import _bar
```