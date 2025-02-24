# reimplemented-operator (FURB118)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for lambda expressions and function definitions that can be replaced with a function from
the operator module.
## Why is this bad?
The operator module provides functions that implement the same functionality as the
corresponding operators. For example, operator.add is often equivalent to lambda x, y: x + y.
Using the functions from the operator module is more concise and communicates the intent of
the code more clearly.
## Example
```
import functools
nums = [1, 2, 3]
total = functools.reduce(lambda x, y: x + y, nums)
```
## Use instead:
```
import functools
import operator
nums = [1, 2, 3]
total = functools.reduce(operator.add, nums)
Fix safety
The fix offered by this rule is always marked as unsafe. While the changes the fix would make
would rarely break your code, there are two ways in which functions from the operator module
differ from user-defined functions. It would be non-trivial for Ruff to detect whether or not
these differences would matter in a specific situation where Ruff is emitting a diagnostic for
this rule.
The first difference is that operator functions cannot be called with keyword arguments, but
most user-defined functions can. If an add function is defined as add = lambda x, y: x + y,
replacing this function with operator.add will cause the later call to raise TypeError if
the function is later called with keyword arguments, e.g. add(x=1, y=2).
The second difference is that user-defined functions are descriptors, but this is not true of
the functions defined in the operator module. Practically speaking, this means that defining
a function in a class body (either by using a def statement or assigning a lambda function
to a variable) is a valid way of defining an instance method on that class; monkeypatching a
user-defined function onto a class after the class has been created also has the same effect.
The same is not true of an operator function: assigning an operator function to a variable
in a class body or monkeypatching one onto a class will not create a valid instance method.
Ruff will refrain from emitting diagnostics for this rule on function definitions in class
bodies; however, it does not currently have sophisticated enough type inference to avoid
emitting this diagnostic if a user-defined function is being monkeypatched onto a class after
the class has been constructed.
```