# unnecessary-iterable-allocation-for-first-element (RUF015)
Fix is always available.
## What it does
Checks the following constructs, all of which can be replaced by
next(iter(...)):
list(...)[0]
tuple(...)[0]
list(i for i in ...)[0]
[i for i in ...][0]
list(...).pop(0)
## Why is this bad?
Calling e.g. list(...) will create a new list of the entire collection,
which can be very expensive for large collections. If you only need the
first element of the collection, you can use next(...) or
next(iter(...) to lazily fetch the first element. The same is true for
the other constructs.
## Example
```
head = list(x)[0]
head = [x * x for x in range(10)][0]
```
## Use instead:
```
head = next(iter(x))
head = next(x * x for x in range(10))
Fix safety
This rule's fix is marked as unsafe, as migrating from (e.g.) list(...)[0]
to next(iter(...)) can change the behavior of your program in two ways:
First, all above-mentioned constructs will eagerly evaluate the entire
    collection, while next(iter(...)) will only evaluate the first
    element. As such, any side effects that occur during iteration will be
    delayed.
Second, accessing members of a collection via square bracket notation
    [0] of the pop() function will raise IndexError if the collection
    is empty, while next(iter(...)) will raise StopIteration.
```