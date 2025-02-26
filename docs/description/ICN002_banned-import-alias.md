# banned-import-alias (ICN002)
Derived from the flake8-import-conventions linter.
## What it does
Checks for imports that use non-standard naming conventions, like
import tensorflow.keras.backend as K.
## Why is this bad?
Consistency is good. Avoid using a non-standard naming convention for
imports, and, in particular, choosing import aliases that violate PEP 8.
For example, aliasing via import tensorflow.keras.backend as K violates
the guidance of PEP 8, and is thus avoided in some projects.
## Example
```
import tensorflow.keras.backend as K
```
## Use instead:
```
import tensorflow as tf
tf.keras.backend
```