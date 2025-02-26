# dot-format-in-exception (EM103)
Derived from the flake8-errmsg linter.
Fix is sometimes available.
## What it does
Checks for the use of .format calls on string literals in exception
constructors.
## Why is this bad?
Python includes the raise in the default traceback (and formatters
like Rich and IPython do too).
By using a .format call, the error message will be duplicated in the
traceback, which can make the traceback less readable.
## Example
```
Given:
sub = "Some value"
raise RuntimeError("'{}' is incorrect".format(sub))
Python will produce a traceback like:
Traceback (most recent call last):
  File "tmp.py", line 2, in <module>
    raise RuntimeError("'{}' is incorrect".format(sub))
RuntimeError: 'Some value' is incorrect
Instead, assign the string to a variable:
sub = "Some value"
msg = "'{}' is incorrect".format(sub)
raise RuntimeError(msg)
Which will produce a traceback like:
Traceback (most recent call last):
  File "tmp.py", line 3, in <module>
    raise RuntimeError(msg)
RuntimeError: 'Some value' is incorrect
```