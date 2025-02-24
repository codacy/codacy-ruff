# subclass-builtin (FURB189)
Derived from the refurb linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for subclasses of dict, list or str.
## Why is this bad?
Subclassing dict, list, or str objects can be error prone, use the
UserDict, UserList, and UserString objects from the collections module
instead.
## Example
```
class CaseInsensitiveDict(dict): ...
```
## Use instead:
```
from collections import UserDict
class CaseInsensitiveDict(UserDict): ...
Fix safety
This fix is marked as unsafe because isinstance() checks for dict,
list, and str types will fail when using the corresponding User class.
If you need to pass custom dict or list objects to code you don't
control, ignore this check. If you do control the code, consider using
the following type checks instead:
dict -> collections.abc.MutableMapping
list -> collections.abc.MutableSequence
str -> No such conversion exists
```