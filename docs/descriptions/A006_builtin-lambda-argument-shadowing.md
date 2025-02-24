# builtin-lambda-argument-shadowing (A006)
Derived from the flake8-builtins linter.
## What it does
Checks for lambda arguments that use the same names as Python builtins.
## Why is this bad?
Reusing a builtin name for the name of a lambda argument increases the
difficulty of reading and maintaining the code and can cause
non-obvious errors. Readers may mistake the variable for the
builtin, and vice versa.
Builtins can be marked as exceptions to this rule via the
lint.flake8-builtins.builtins-ignorelist configuration option.
```