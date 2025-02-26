# boolean-positional-value-in-call (FBT003)
Derived from the flake8-boolean-trap linter.
## What it does
Checks for boolean positional arguments in function calls.
Some functions are whitelisted by default. To extend the list of allowed calls
configure the lint.flake8-boolean-trap.extend-allowed-calls option.
## Why is this bad?
Calling a function with boolean positional arguments is confusing as the
meaning of the boolean value is not clear to the caller, and to future
readers of the code.
## Example
```
def func(flag: bool) -> None: ...
func(True)
```
## Use instead:
```
def func(flag: bool) -> None: ...
func(flag=True)
```