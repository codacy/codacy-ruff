# bad-quotes-multiline-string (Q001)
Derived from the flake8-quotes linter.
Fix is always available.
## What it does
Checks for multiline strings that use single quotes or double quotes,
depending on the value of the lint.flake8-quotes.multiline-quotes
setting.
## Why is this bad?
Consistency is good. Use either single or double quotes for multiline
strings, but be consistent.
## Example
```
foo = '''
bar
'''
Assuming multiline-quotes is set to double, use instead:
foo = """
bar
"""
```