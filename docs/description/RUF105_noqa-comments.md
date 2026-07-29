# noqa-comments (RUF105)
Preview (since 0.15.22) ·
Related issues ·
View source
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for the use of noqa comments instead of Ruff-specific ruff: ignore comments.
## Why is this bad?
ruff: ignore comments allow the use of rule names instead of codes and can be used in more
places than noqa comments.
Note that this is an opinionated, stylistic rule. noqa comments may be needed for backwards
compatibility with other tools. You should also feel free to disable this rule if you simply
prefer noqa comments.
## Example
```
import os  # noqa: F401
```
## Use instead:
```
import os  # ruff: ignore[F401]
Or if you prefer the own-line form:
# ruff: ignore[unused-import]
import os
```