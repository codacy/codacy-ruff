# no-explicit-stacklevel (B028)
Derived from the flake8-bugbear linter.
Fix is always available.
## What it does
Checks for warnings.warn calls without an explicit stacklevel keyword
argument.
## Why is this bad?
The warnings.warn method uses a stacklevel of 1 by default, which
will output a stack frame of the line on which the "warn" method
is called. Setting it to a higher number will output a stack frame
from higher up the stack.
It's recommended to use a stacklevel of 2 or higher, to give the caller
more context about the warning.
## Example
```
warnings.warn("This is a warning")
```
## Use instead:
```
warnings.warn("This is a warning", stacklevel=2)
Fix safety
This rule's fix is marked as unsafe because it changes
the behavior of the code. Moreover, the fix will assign
a stacklevel of 2, while the user may wish to assign a
higher stacklevel to address the diagnostic.
```