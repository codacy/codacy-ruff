# map-int-version-parsing (RUF048)
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for calls of the form map(int, __version__.split(".")).
## Why is this bad?
__version__ does not always contain integral-like elements.
import matplotlib  # `__version__ == "3.9.1.post-1"` in our environment
# ValueError: invalid literal for int() with base 10: 'post1'
tuple(map(int, matplotlib.__version__.split(".")))
See also Version specifiers | Packaging spec.
## Example
```
tuple(map(int, matplotlib.__version__.split(".")))
```
## Use instead:
```
import packaging.version as version
version.parse(matplotlib.__version__)
```