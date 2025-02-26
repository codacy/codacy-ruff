# triple-single-quotes (D300)
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for docstrings that use '''triple single quotes''' instead of
"""triple double quotes""".
## Why is this bad?
PEP 257 recommends
the use of """triple double quotes""" for docstrings, to ensure
consistency.
## Example
```
def kos_root():
    '''Return the pathname of the KOS root directory.'''
```
## Use instead:
```
def kos_root():
    """Return the pathname of the KOS root directory."""
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter enforces consistent quotes, making the rule redundant.
```