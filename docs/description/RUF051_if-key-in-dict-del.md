# if-key-in-dict-del (RUF051)
Added in 0.10.0 ·
Related issues ·
View source
Fix is always available.
## What it does
Checks for if key in dictionary: del dictionary[key].
## Why is this bad?
To remove a key-value pair from a dictionary, it's more concise to use .pop(..., None).
## Example
```
dictionary = {}
if key in dictionary:
    del dictionary[key]
```
## Use instead:
```
dictionary = {}
dictionary.pop(key, None)
Fix safety
This rule's fix is marked as safe, unless the if statement contains comments.
```