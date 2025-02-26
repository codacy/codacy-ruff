# unsorted-dunder-slots (RUF023)
Fix is sometimes available.
## What it does
Checks for __slots__ definitions that are not ordered according to a
natural sort.
## Why is this bad?
Consistency is good. Use a common convention for this special variable
to make your code more readable and idiomatic.
## Example
```
class Dog:
    __slots__ = "name", "breed"
```
## Use instead:
```
class Dog:
    __slots__ = "breed", "name"
Fix safety
This rule's fix is marked as unsafe in three situations.
Firstly, the fix is unsafe if there are any comments that take up
a whole line by themselves inside the __slots__ definition, for example:
class Foo:
    __slots__ = [
        # eggy things
        "duck_eggs",
        "chicken_eggs",
        # hammy things
        "country_ham",
        "parma_ham",
    ]
This is a common pattern used to delimit categories within a class's slots,
but it would be out of the scope of this rule to attempt to maintain these
categories when applying a natural sort to the items of __slots__.
Secondly, the fix is also marked as unsafe if there are more than two
__slots__ items on a single line and that line also has a trailing
comment, since here it is impossible to accurately gauge which item the
comment should be moved with when sorting __slots__:
class Bar:
    __slots__ = [
        "a", "c", "e",  # a comment
        "b", "d", "f",  # a second  comment
    ]
Lastly, this rule's fix is marked as unsafe whenever Ruff can detect that
code elsewhere in the same file reads the __slots__ variable in some way
and the __slots__ variable is not assigned to a set. This is because the
order of the items in __slots__ may have semantic significance if the
__slots__ of a class is being iterated over, or being assigned to another
value.
In the vast majority of other cases, this rule's fix is unlikely to
cause breakage; as such, Ruff will otherwise mark this rule's fix as
safe. However, note that (although it's rare) the value of __slots__
could still be read by code outside of the module in which the
__slots__ definition occurs, in which case this rule's fix could
theoretically cause breakage.
```