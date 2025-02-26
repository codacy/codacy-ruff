# multi-value-repeated-key-variable (F602)
Derived from the Pyflakes linter.
Fix is sometimes available.
## What it does
Checks for dictionary keys that are repeated with different values.
## Why is this bad?
Dictionary keys should be unique. If a key is repeated with a different
value, the first values will be overwritten and the key will correspond to
the last value. This is likely a mistake.
## Example
```
foo = {
    bar: 1,
    baz: 2,
    baz: 3,
}
foo[baz]  # 3
```
## Use instead:
```
foo = {
    bar: 1,
    baz: 2,
}
foo[baz]  # 2
```