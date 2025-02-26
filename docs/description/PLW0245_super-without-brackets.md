# super-without-brackets (PLW0245)
Derived from the Pylint linter.
Fix is always available.
## What it does
Detects attempts to use super without parentheses.
## Why is this bad?
The super() callable
can be used inside method definitions to create a proxy object that
delegates attribute access to a superclass of the current class. Attempting
to access attributes on super itself, however, instead of the object
returned by a call to super(), will raise AttributeError.
## Example
```
class Animal:
    @staticmethod
    def speak():
        return "This animal says something."
class Dog(Animal):
    @staticmethod
    def speak():
        original_speak = super.speak()  # ERROR: `super.speak()`
        return f"{original_speak} But as a dog, it barks!"
```
## Use instead:
```
class Animal:
    @staticmethod
    def speak():
        return "This animal says something."
class Dog(Animal):
    @staticmethod
    def speak():
        original_speak = super().speak()  # Correct: `super().speak()`
        return f"{original_speak} But as a dog, it barks!"
```