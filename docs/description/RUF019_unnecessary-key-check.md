# unnecessary-key-check (RUF019)
Fix is always available.
## What it does
Checks for unnecessary key checks prior to accessing a dictionary.
## Why is this bad?
When working with dictionaries, the get can be used to access a value
without having to check if the dictionary contains the relevant key,
returning None if the key is not present.
## Example
```
if "key" in dct and dct["key"]:
    ...
```
## Use instead:
```
if dct.get("key"):
    ...
```