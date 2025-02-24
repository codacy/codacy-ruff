# if-key-in-dict-del (RUF051)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for if key in dictionary: del dictionary[key].
## Why is this bad?
To remove a key-value pair from a dictionary, it's more concise to use .pop(..., None).
## Example
```
if key in dictionary:
    del dictionary[key]
```
## Use instead:
```
dictionary.pop(key, None)
Fix safety
This rule's fix is marked as safe, unless the if statement contains comments.
```