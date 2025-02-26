# return-in-init (PLE0101)
Derived from the Pylint linter.
## What it does
Checks for __init__ methods that return values.
## Why is this bad?
The __init__ method is the constructor for a given Python class,
responsible for initializing, rather than creating, new objects.
The __init__ method has to return None. Returning any value from
an __init__ method will result in a runtime error.
## Example
```
class Example:
    def __init__(self):
        return []
```
## Use instead:
```
class Example:
    def __init__(self):
        self.value = []
```