# f-string-in-exception (EM102)
Derived from the flake8-errmsg linter.
Fix is sometimes available.
## What it does
Checks for the use of f-strings in exception constructors.
## Why is this bad?
Python includes the raise in the default traceback (and formatters
like Rich and IPython do too).
By using an f-string, the error message will be duplicated in the
traceback, which can make the traceback less readable.
## Example
```
Given:
sub = "Some value"
raise RuntimeError(f"{sub!r} is incorrect")
Python will produce a traceback like:
Traceback (most recent call last):
  File "tmp.py", line 2, in <module>
    raise RuntimeError(f"{sub!r} is incorrect")
RuntimeError: 'Some value' is incorrect
Instead, assign the string to a variable:
sub = "Some value"
msg = f"{sub!r} is incorrect"
raise RuntimeError(msg)
Which will produce a traceback like:
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    raise RuntimeError(msg)
RuntimeError: 'Some value' is incorrect
```