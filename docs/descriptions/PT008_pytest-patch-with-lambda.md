# pytest-patch-with-lambda (PT008)
Derived from the flake8-pytest-style linter.
## What it does
Checks for mocked calls that use a dummy lambda function instead of
return_value.
## Why is this bad?
When patching calls, an explicit return_value better conveys the intent
than a lambda function, assuming the lambda does not use the arguments
passed to it.
return_value is also robust to changes in the patched function's
signature, and enables additional assertions to verify behavior. For
example, return_value allows for verification of the number of calls or
the arguments passed to the patched function via assert_called_once_with
and related methods.
## Example
```
def test_foo(mocker):
    mocker.patch("module.target", lambda x, y: 7)
```
## Use instead:
```
def test_foo(mocker):
    mocker.patch("module.target", return_value=7)
    # If the lambda makes use of the arguments, no diagnostic is emitted.
    mocker.patch("module.other_target", lambda x, y: x)
```