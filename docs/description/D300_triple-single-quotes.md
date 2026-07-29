# triple-single-quotes (D300)
Added in v0.0.69 ·
Related issues ·
View source
Derived from the pydocstyle linter.
Fix is sometimes available.
## What it does
Checks for docstrings that don't use """triple double quotes""".
## Why is this bad?
PEP 257 recommends
the use of """triple double quotes""" for docstrings, to ensure
consistency.
## Example
```
def kos_root():
    '''Return the pathname of the KOS root directory.'''
def kos_branch():
    'Return the branch name.'
```
## Use instead:
```
def kos_root():
    """Return the pathname of the KOS root directory."""
def kos_branch():
    """Return the branch name."""
Formatter compatibility
We recommend against using this rule alongside the formatter. The
formatter enforces consistent quotes, making the rule redundant.
```