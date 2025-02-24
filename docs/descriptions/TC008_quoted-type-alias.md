# quoted-type-alias (TC008)
Derived from the flake8-type-checking linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for unnecessary quotes in PEP 613 explicit type aliases
and PEP 695 type statements.
## Why is this bad?
Unnecessary string forward references can lead to additional overhead
in runtime libraries making use of type hints. They can also have bad
interactions with other runtime uses like PEP 604 type unions.
PEP-613 type aliases are only flagged by the rule if Ruff can have high
confidence that the quotes are unnecessary. Specifically, any PEP-613
type alias where the type expression on the right-hand side contains
subscripts or attribute accesses will not be flagged. This is because
type aliases can reference types that are, for example, generic in stub
files but not at runtime. That can mean that a type checker expects the
referenced type to be subscripted with type arguments despite the fact
that doing so would fail at runtime if the type alias value was not
quoted. Similarly, a type alias might need to reference a module-level
attribute that exists in a stub file but not at runtime, meaning that
the type alias value would need to be quoted to avoid a runtime error.
## Example
```
Given:
OptInt: TypeAlias = "int | None"
```
## Use instead:
```
OptInt: TypeAlias = int | None
Given:
type OptInt = "int | None"
```
## Use instead:
```
type OptInt = int | None
Fix safety
This rule's fix is marked as safe, unless the type annotation contains comments.
See also
This rule only applies to type aliases in non-stub files. For removing quotes in other
contexts or in stub files, see:
quoted-annotation-in-stub: A rule that
    removes all quoted annotations from stub files
quoted-annotation: A rule that removes unnecessary quotes
    from annotations in runtime files.
```