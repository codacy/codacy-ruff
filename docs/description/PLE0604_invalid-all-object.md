# invalid-all-object (PLE0604)
Added in v0.0.237 ·
Related issues ·
View source
Derived from the Pylint linter.
## What it does
Checks for the inclusion of invalid objects in __all__.
## Why is this bad?
In Python, __all__ should contain a sequence of strings that represent
the names of all "public" symbols exported by a module.
Assigning anything other than a tuple or list of strings to __all__
is invalid.
## Example
```
__all__ = [Foo, 1, None]
```
## Use instead:
```
__all__ = ["Foo", "Bar", "Baz"]
```