# raw-string-in-exception (EM101)
Derived from the flake8-errmsg linter.
Fix is sometimes available.
## What it does
Checks for the use of string literals in exception constructors.
## Why is this bad?
Python includes the raise in the default traceback (and formatters
like Rich and IPython do too).
By using a string literal, the error message will be duplicated in the
traceback, which can make the traceback less readable.
## Example
```
Given:
raise RuntimeError("'Some value' is incorrect")
Python will produce a traceback like:
Traceback (most recent call last):
  File "tmp.py", line 2, in <module>
    raise RuntimeError("'Some value' is incorrect")
RuntimeError: 'Some value' is incorrect
Instead, assign the string to a variable:
msg = "'Some value' is incorrect"
raise RuntimeError(msg)
Which will produce a traceback like:
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    raise RuntimeError(msg)
RuntimeError: 'Some value' is incorrect
```