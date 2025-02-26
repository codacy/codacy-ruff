# invalid-character-backspace (PLE2510)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for strings that contain the control character BS.
## Why is this bad?
Control characters are displayed differently by different text editors and
terminals.
By using the \b sequence in lieu of the BS control character, the
string will contain the same value, but will render visibly in all editors.
## Example
```
x = ""
```
## Use instead:
```
x = "\b"
```