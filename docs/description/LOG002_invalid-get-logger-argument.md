# invalid-get-logger-argument (LOG002)
Derived from the flake8-logging linter.
Fix is sometimes available.
## What it does
Checks for any usage of __cached__ and __file__ as an argument to
logging.getLogger().
## Why is this bad?
The logging documentation recommends this pattern:
logging.getLogger(__name__)
Here, __name__ is the fully qualified module name, such as foo.bar,
which is the intended format for logger names.
This rule detects probably-mistaken usage of similar module-level dunder constants:
__cached__ - the pathname of the module's compiled version, such as foo/__pycache__/bar.cpython-311.pyc.
__file__ - the pathname of the module, such as foo/bar.py.
## Example
```
import logging
logger = logging.getLogger(__file__)
```
## Use instead:
```
import logging
logger = logging.getLogger(__name__)
```