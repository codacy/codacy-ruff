# lazy-import-mismatch (TID254)
Preview (since 0.15.6) ·
Related issues ·
View source
Derived from the flake8-tidy-imports linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Enforces the configured lazy-import policy in contexts where lazy import
is legal.
## Why is this bad?
Python 3.15 adds support for lazy import and lazy from ... import ...,
which defer the actual import work until the imported name is first used.
Depending on the policy, some modules should be imported lazily to defer
import work until the name is first used, while others should remain eager
to preserve import-time side effects.
This rule ignores contexts in which lazy import is invalid, such as
functions, classes, try/except blocks, __future__ imports, and
from ... import * statements.
## Example
```
import typing
```
## Use instead:
```
lazy import typing
```