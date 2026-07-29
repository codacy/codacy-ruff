# unused-annotation (F842)
Added in v0.0.172 ·
Related issues ·
View source
Derived from the Pyflakes linter.
## What it does
Checks for local variables that are annotated but never used.
## Why is this bad?
Annotations are used to provide type hints to static type checkers. If a
variable is annotated but never used, the annotation is unnecessary.
## Example
```
def foo():
    bar: int
```