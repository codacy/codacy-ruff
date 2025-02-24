# import-outside-top-level (PLC0415)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for import statements outside of a module's top-level scope, such
as within a function or class definition.
## Why is this bad?
PEP 8 recommends placing imports not only at the top-level of a module,
but at the very top of the file, "just after any module comments and
docstrings, and before module globals and constants."
import statements have effects that are global in scope; defining them at
the top level has a number of benefits. For example, it makes it easier to
identify the dependencies of a module, and ensures that any invalid imports
are caught regardless of whether a specific function is called or class is
instantiated.
An import statement would typically be placed within a function only to
avoid a circular dependency, to defer a costly module load, or to avoid
loading a dependency altogether in a certain runtime environment.
## Example
```
def print_python_version():
    import platform
    print(python.python_version())
```
## Use instead:
```
import platform
def print_python_version():
    print(python.python_version())
```