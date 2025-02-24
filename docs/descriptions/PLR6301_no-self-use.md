# no-self-use (PLR6301)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for the presence of unused self parameter in methods definitions.
## Why is this bad?
Unused self parameters are usually a sign of a method that could be
replaced by a function, class method, or static method.
## Example
```
class Person:
    def greeting(self):
        print("Greetings friend!")
```
## Use instead:
```
def greeting():
    print("Greetings friend!")
or
class Person:
    @staticmethod
    def greeting():
        print("Greetings friend!")
```