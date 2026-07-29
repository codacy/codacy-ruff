# invalid-mock-access (PGH005)
Added in v0.0.266 ·
Related issues ·
View source
Derived from the pygrep-hooks linter.
## What it does
Checks for common mistakes when using mock objects.
## Why is this bad?
The mock module exposes an assertion API that can be used to verify that
mock objects undergo expected interactions. This rule checks for common
mistakes when using this API.
For example, it checks for mock attribute accesses that should be replaced
with mock method calls.
## Example
```
my_mock.assert_called
```
## Use instead:
```
my_mock.assert_called()
```