# too-many-blank-lines (E303)
Derived from the pycodestyle linter.
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for extraneous blank lines.
## Why is this bad?
PEP 8 recommends using blank lines as follows:
No more than two blank lines between top-level statements.
No more than one blank line between non-top-level statements.
## Example
```
def func1():
    pass
def func2():
    pass
```
## Use instead:
```
def func1():
    pass
def func2():
    pass
Typing stub files (.pyi)
The rule allows at most one blank line in typing stub files in accordance to the typing style guide recommendation.
Note: The rule respects the following isort settings when determining the maximum number of blank lines allowed between two statements:
lint.isort.lines-after-imports: For top-level statements directly following an import statement.
lint.isort.lines-between-types: For import statements directly following a from ... import ... statement or vice versa.
```