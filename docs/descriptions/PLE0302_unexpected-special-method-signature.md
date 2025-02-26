# unexpected-special-method-signature (PLE0302)
Derived from the Pylint linter.
## What it does
Checks for "special" methods that have an unexpected method signature.
## Why is this bad?
"Special" methods, like __len__, are expected to adhere to a specific,
standard function signature. Implementing a "special" method using a
non-standard function signature can lead to unexpected and surprising
behavior for users of a given class.
## Example
```
class Bookshelf:
    def __init__(self):
        self._books = ["Foo", "Bar", "Baz"]
    def __len__(self, index):  # __len__ does not except an index parameter
        return len(self._books)
    def __getitem__(self, index):
        return self._books[index]
```
## Use instead:
```
class Bookshelf:
    def __init__(self):
        self._books = ["Foo", "Bar", "Baz"]
    def __len__(self):
        return len(self._books)
    def __getitem__(self, index):
        return self._books[index]
```