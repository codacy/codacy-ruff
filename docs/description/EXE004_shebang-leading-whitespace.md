# shebang-leading-whitespace (EXE004)
Derived from the flake8-executable linter.
Fix is always available.
## What it does
Checks for whitespace before a shebang directive.
## Why is this bad?
In Python, a shebang (also known as a hashbang) is the first line of a
script, which specifies the interpreter that should be used to run the
script.
The shebang's #! prefix must be the first two characters of a file. The
presence of whitespace before the shebang will cause the shebang to be
ignored, which is likely a mistake.
## Example
```
 #!/usr/bin/env python3
```
## Use instead:
```
#!/usr/bin/env python3
```