# invalid-character-esc (PLE2513)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for strings that contain the raw control character ESC.
## Why is this bad?
Control characters are displayed differently by different text editors and
terminals.
By using the \x1B sequence in lieu of the SUB control character, the
string will contain the same value, but will render visibly in all editors.
## Example
```
x = ""
```
## Use instead:
```
x = "\x1b"
```