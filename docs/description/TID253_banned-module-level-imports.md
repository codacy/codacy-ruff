# banned-module-level-imports (TID253)
Derived from the flake8-tidy-imports linter.
## What it does
Checks for module-level imports that should instead be imported lazily
(e.g., within a function definition, or an if TYPE_CHECKING: block, or
some other nested context).
## Why is this bad?
Some modules are expensive to import. For example, importing torch or
tensorflow can introduce a noticeable delay in the startup time of a
Python program.
In such cases, you may want to enforce that the module is imported lazily
as needed, rather than at the top of the file. This could involve inlining
the import into the function that uses it, rather than importing it
unconditionally, to ensure that the module is only imported when necessary.
## Example
```
import tensorflow as tf
def show_version():
    print(tf.__version__)
```
## Use instead:
```
def show_version():
    import tensorflow as tf
    print(tf.__version__)
```