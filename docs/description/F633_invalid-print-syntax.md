# invalid-print-syntax (F633)
Derived from the Pyflakes linter.
## What it does
Checks for print statements that use the >> syntax.
## Why is this bad?
In Python 2, the print statement can be used with the >> syntax to
print to a file-like object. This print >> sys.stderr syntax no
longer exists in Python 3, where print is only a function, not a
statement.
Instead, use the file keyword argument to the print function, the
sys.stderr.write function, or the logging module.
## Example
```
from __future__ import print_function
import sys
print >> sys.stderr, "Hello, world!"
```
## Use instead:
```
print("Hello, world!", file=sys.stderr)
Or:
import sys
sys.stderr.write("Hello, world!\n")
Or:
import logging
logging.error("Hello, world!")
```