# shebang-leading-whitespace (EXE004)
Added in v0.0.229 ·
Related issues ·
View source
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
Fix safety
This rule's fix is marked as unsafe when the whitespace before the shebang
contains a newline. Deleting the newline can activate an encoding declaration
and change how the file is decoded.
```