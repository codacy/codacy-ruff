# bidirectional-unicode (PLE2502)
Derived from the Pylint linter.
## What it does
Checks for bidirectional unicode characters.
## Why is this bad?
The interaction between bidirectional unicode characters and the
surrounding code can be surprising to those that are unfamiliar
with right-to-left writing systems.
In some cases, bidirectional unicode characters can also be used to
obfuscate code and introduce or mask security vulnerabilities.
## Example
```
s = "א" * 100  #  "א" is assigned
print(s)  # prints a 100-character string
```