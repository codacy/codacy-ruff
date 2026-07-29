# invalid-character-esc (PLE2513)
Added in v0.0.257 ·
Related issues ·
View source
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for strings that contain the raw control character ESC.
## Why is this bad?
Control characters are displayed differently by different text editors and
terminals.
By using the \x1b sequence in lieu of the ESC control character, the
string will contain the same value, but will render visibly in all editors.
## Example
```
x = ""
```
## Use instead:
```
x = "\x1b"
```