# duplicate-entry-in-dunder-all (RUF068)
Added in 0.16.0 ·
Related issues ·
View source
Fix is sometimes available.
## What it does
Detects duplicate elements in __all__ definitions.
## Why is this bad?
Duplicate elements in __all__ serve no purpose and can indicate copy-paste errors or
incomplete refactoring.
## Example
```
__all__ = [
    "DatabaseConnection",
    "Product",
    "User",
    "DatabaseConnection",  # Duplicate
]
```
## Use instead:
```
__all__ = [
    "DatabaseConnection",
    "Product",
    "User",
]
Fix Safety
This rule's fix is marked as unsafe if the replacement would remove comments attached to the
original expression, potentially losing important context or documentation.
For example:
__all__ = [
    "PublicAPI",
    # TODO: Remove this in v2.0
    "PublicAPI",  # Deprecated alias
]
```