# timeout-error-alias (UP041)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for uses of exceptions that alias TimeoutError.
## Why is this bad?
TimeoutError is the builtin error type used for exceptions when a system
function timed out at the system level.
In Python 3.10, socket.timeout was aliased to TimeoutError. In Python
3.11, asyncio.TimeoutError was aliased to TimeoutError.
These aliases remain in place for compatibility with older versions of
Python, but may be removed in future versions.
Prefer using TimeoutError directly, as it is more idiomatic and future-proof.
## Example
```
raise asyncio.TimeoutError
```
## Use instead:
```
raise TimeoutError
```