# lazy-import-immediately-resolved (TID255)
Preview (since 0.15.13) ·
Related issues ·
View source
Derived from the flake8-tidy-imports linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for lazy imports that are resolved immediately at module load time.
## Why is this bad?
Python 3.15 adds support for lazy import and lazy from ... import ...,
which defer the actual import work until the imported name is first used.
When a lazily imported name is used immediately at module load time, the
import is resolved eagerly, defeating the purpose of marking the import as
lazy. This is commonly caused by using a lazily imported module in a module
global or in a top-level class definition.
## Example
```
lazy import foo
class Bar(foo.Foo): ...
```
## Use instead:
```
import foo
class Bar(foo.Foo): ...
Fix safety
This rule's fix is marked as unsafe because converting a lazy import to an
eager import changes when the imported module is executed, which can change
runtime behavior if the module has import-time side effects.
The fix is only available when the lazy import statement imports a single
member, since removing lazy from a multi-member import would make every
imported member eager, including names that may not be resolved immediately.
```