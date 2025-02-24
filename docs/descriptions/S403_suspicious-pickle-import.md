# suspicious-pickle-import (S403)
Derived from the flake8-bandit linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for imports of the pickle, cPickle, dill, and shelve modules.
## Why is this bad?
It is possible to construct malicious pickle data which will execute
arbitrary code during unpickling. Consider possible security implications
associated with these modules.
## Example
```
import pickle
```