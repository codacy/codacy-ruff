# zip-dict-keys-and-values (SIM911)
Derived from the flake8-simplify linter.
Fix is always available.
## What it does
Checks for use of zip() to iterate over keys and values of a dictionary at once.
## Why is this bad?
The dict type provides an .items() method which is faster and more readable.
## Example
```
flag_stars = {"USA": 50, "Slovenia": 3, "Panama": 2, "Australia": 6}
for country, stars in zip(flag_stars.keys(), flag_stars.values()):
    print(f"{country}'s flag has {stars} stars.")
```
## Use instead:
```
flag_stars = {"USA": 50, "Slovenia": 3, "Panama": 2, "Australia": 6}
for country, stars in flag_stars.items():
    print(f"{country}'s flag has {stars} stars.")
```