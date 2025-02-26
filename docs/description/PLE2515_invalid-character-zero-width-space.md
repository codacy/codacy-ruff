# invalid-character-zero-width-space (PLE2515)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for strings that contain the zero width space character.
## Why is this bad?
This character is rendered invisibly in some text editors and terminals.
By using the \u200B sequence, the string will contain the same value,
but will render visibly in all editors.
## Example
```
x = "Dear Sir/Madam"
```
## Use instead:
```
x = "Dear Sir\u200b/\u200bMadam"  # zero width space
```