# stdlib-module-shadowing (A005)
Derived from the flake8-builtins linter.
## What it does
Checks for modules that use the same names as Python standard-library
modules.
## Why is this bad?
Reusing a standard-library module name for the name of a module increases
the difficulty of reading and maintaining the code, and can cause
non-obvious errors. Readers may mistake the first-party module for the
standard-library module and vice versa.
Standard-library modules can be marked as exceptions to this rule via the
lint.flake8-builtins.allowed-modules configuration option.
By default, the module path relative to the project root or src directories is considered,
so a top-level logging.py or logging/__init__.py will clash with the builtin logging
module, but utils/logging.py, for example, will not. With the
lint.flake8-builtins.strict-checking option set to true, only the last component
of the module name is considered, so logging.py, utils/logging.py, and
utils/logging/__init__.py will all trigger the rule.
This rule is not applied to stub files, as the name of a stub module is out
of the control of the author of the stub file. Instead, a stub should aim to
faithfully emulate the runtime module it is stubbing.
As of Python 3.13, errors from modules that use the same name as
standard-library modules now display a custom message.
## Example
```
$ touch random.py
$ python3 -c 'from random import choice'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    from random import choice
ImportError: cannot import name 'choice' from 'random' (consider renaming '/random.py' since it has the same name as the standard library module named 'random' and prevents importing that standard library module)
```