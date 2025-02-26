# useless-exception-statement (PLW0133)
Derived from the Pylint linter.
Fix is sometimes available.
## What it does
Checks for an exception that is not raised.
## Why is this bad?
It's unnecessary to create an exception without raising it. For example,
ValueError("...") on its own will have no effect (unlike
raise ValueError("...")) and is likely a mistake.
Known problems
This rule only detects built-in exceptions, like ValueError, and does
not catch user-defined exceptions.
## Example
```
ValueError("...")
```
## Use instead:
```
raise ValueError("...")
Fix safety
This rule's fix is marked as unsafe, as converting a useless exception
statement to a raise statement will change the program's behavior.
```