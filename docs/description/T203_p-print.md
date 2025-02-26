# p-print (T203)
Derived from the flake8-print linter.
Fix is sometimes available.
## What it does
Checks for pprint statements.
## Why is this bad?
Like print statements, pprint statements are useful in some situations
(e.g., debugging), but should typically be omitted from production code.
pprint statements can lead to the accidental inclusion of sensitive
information in logs, and are not configurable by clients, unlike logging
statements.
## Example
```
import pprint
def merge_dicts(dict_a, dict_b):
    dict_c = {**dict_a, **dict_b}
    pprint.pprint(dict_c)
    return dict_c
```
## Use instead:
```
def merge_dicts(dict_a, dict_b):
    dict_c = {**dict_a, **dict_b}
    return dict_c
Fix safety
This rule's fix is marked as unsafe, as it may remove pprint statements
that are used beyond debugging purposes.
```