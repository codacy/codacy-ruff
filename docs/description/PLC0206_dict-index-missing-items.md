# dict-index-missing-items (PLC0206)
Derived from the Pylint linter.
## What it does
Checks for dictionary iterations that extract the dictionary value
via explicit indexing, instead of using .items().
## Why is this bad?
Iterating over a dictionary with .items() is semantically clearer
and more efficient than extracting the value with the key.
## Example
```
ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}
for instrument in ORCHESTRA:
    print(f"{instrument}: {ORCHESTRA[instrument]}")
```
## Use instead:
```
ORCHESTRA = {
    "violin": "strings",
    "oboe": "woodwind",
    "tuba": "brass",
    "gong": "percussion",
}
for instrument, section in ORCHESTRA.items():
    print(f"{instrument}: {section}")
```