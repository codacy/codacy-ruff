# duplicate-literal-member (PYI062)
Derived from the flake8-pyi linter.
Fix is always available.
## What it does
Checks for duplicate members in a typing.Literal[] slice.
## Why is this bad?
Duplicate literal members are redundant and should be removed.
## Example
```
foo: Literal["a", "b", "a"]
```
## Use instead:
```
foo: Literal["a", "b"]
Fix safety
This rule's fix is marked as safe, unless the type annotation contains comments.
Note that while the fix may flatten nested literals into a single top-level literal,
the semantics of the annotation will remain unchanged.
```