# legacy-form-pytest-raises (RUF061)
Added in 0.15.0 ·
Related issues ·
View source
Fix is sometimes available.
## What it does
Checks for non-context-manager use of pytest.raises, pytest.warns, and pytest.deprecated_call.
## Why is this bad?
The context-manager form is more readable, easier to extend, and supports additional keyword
arguments.
## Example
```
import pytest
excinfo = pytest.raises(ValueError, int, "hello")
pytest.warns(UserWarning, my_function, arg)
pytest.deprecated_call(my_deprecated_function, arg1, arg2)
```
## Use instead:
```
import pytest
with pytest.raises(ValueError) as excinfo:
    int("hello")
with pytest.warns(UserWarning):
    my_function(arg)
with pytest.deprecated_call():
    my_deprecated_function(arg1, arg2)
```