# multi-value-repeated-key-literal (F601)
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for dictionary literals that associate multiple values with the
same key.
## Why is this bad?
Dictionary keys should be unique. If a key is associated with multiple values,
the earlier values will be overwritten. Including multiple values for the
same key in a dictionary literal is likely a mistake.
## Example
```
foo = {
    "bar": 1,
    "baz": 2,
    "baz": 3,
}
foo["baz"]  # 3
```
## Use instead:
```
foo = {
    "bar": 1,
    "baz": 2,
}
foo["baz"]  # 2
```