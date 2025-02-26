# invalid-character-nul (PLE2514)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for strings that contain the raw control character NUL (0 byte).
## Why is this bad?
Control characters are displayed differently by different text editors and
terminals.
By using the \0 sequence in lieu of the NUL control character, the
string will contain the same value, but will render visibly in all editors.
## Example
```
x = ""
```
## Use instead:
```
x = "\0"
```