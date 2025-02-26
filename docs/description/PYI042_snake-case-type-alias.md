# snake-case-type-alias (PYI042)
Derived from the flake8-pyi linter.
## What it does
Checks for type aliases that do not use the CamelCase naming convention.
## Why is this bad?
It's conventional to use the CamelCase naming convention for type aliases,
to distinguish them from other variables.
## Example
```
type_alias_name: TypeAlias = int
```
## Use instead:
```
TypeAliasName: TypeAlias = int
```