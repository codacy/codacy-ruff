# incorrect-dict-iterator (PERF102)
Derived from the Perflint linter.
Fix is always available.
## What it does
Checks for uses of dict.items() that discard either the key or the value
when iterating over the dictionary.
## Why is this bad?
If you only need the keys or values of a dictionary, you should use
dict.keys() or dict.values() respectively, instead of dict.items().
These specialized methods are more efficient than dict.items(), as they
avoid allocating tuples for every item in the dictionary. They also
communicate the intent of the code more clearly.
Note that, as with all perflint rules, this is only intended as a
micro-optimization, and will have a negligible impact on performance in
most cases.
## Example
```
obj = {"a": 1, "b": 2}
for key, value in obj.items():
    print(value)
```
## Use instead:
```
obj = {"a": 1, "b": 2}
for value in obj.values():
    print(value)
Fix safety
The fix does not perform any type analysis and, as such, may suggest an
incorrect fix if the object in question does not duck-type as a mapping
(e.g., if it is missing a .keys() or .values() method, or if those
methods behave differently than they do on standard mapping types).
```