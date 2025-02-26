# load-before-global-declaration (PLE0118)
Derived from the Pylint linter.
## What it does
Checks for uses of names that are declared as global prior to the
relevant global declaration.
## Why is this bad?
The global declaration applies to the entire scope. Using a name that's
declared as global in a given scope prior to the relevant global
declaration is a SyntaxError.
## Example
```
counter = 1
def increment():
    print(f"Adding 1 to {counter}")
    global counter
    counter += 1
```
## Use instead:
```
counter = 1
def increment():
    global counter
    print(f"Adding 1 to {counter}")
    counter += 1
```