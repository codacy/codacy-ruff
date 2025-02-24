# eq-without-hash (PLW1641)
Derived from the Pylint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for classes that implement __eq__ but not __hash__.
## Why is this bad?
A class that implements __eq__ but not __hash__ will have its hash
method implicitly set to None, regardless of if a super class defines
__hash__. This will cause the class to be unhashable, will in turn
cause issues when using the class as a key in a dictionary or a member
of a set.
## Example
```
class Person:
    def __init__(self):
        self.name = "monty"
    def __eq__(self, other):
        return isinstance(other, Person) and other.name == self.name
```
## Use instead:
```
class Person:
    def __init__(self):
        self.name = "monty"
    def __eq__(self, other):
        return isinstance(other, Person) and other.name == self.name
    def __hash__(self):
        return hash(self.name)
This issue is particularly tricky with inheritance. Even if a parent class correctly implements
both __eq__ and __hash__, overriding __eq__ in a child class without also implementing
__hash__ will make the child class unhashable:
class Person:
    def __init__(self):
        self.name = "monty"
    def __eq__(self, other):
        return isinstance(other, Person) and other.name == self.name
    def __hash__(self):
        return hash(self.name)
class Developer(Person):
    def __init__(self):
        super().__init__()
        self.language = "python"
    def __eq__(self, other):
        return (
            super().__eq__(other)
            and isinstance(other, Developer)
            and self.language == other.language
        )
hash(Developer())  # TypeError: unhashable type: 'Developer'
One way to fix this is to retain the implementation of __hash__ from the parent class:
class Developer(Person):
    def __init__(self):
        super().__init__()
        self.language = "python"
    def __eq__(self, other):
        return (
            super().__eq__(other)
            and isinstance(other, Developer)
            and self.language == other.language
        )
    __hash__ = Person.__hash__
```