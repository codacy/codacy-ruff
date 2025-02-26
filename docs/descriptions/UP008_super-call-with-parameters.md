# super-call-with-parameters (UP008)
Derived from the pyupgrade linter.
Fix is always available.
## What it does
Checks for super calls that pass redundant arguments.
## Why is this bad?
In Python 3, super can be invoked without any arguments when: (1) the
first argument is __class__, and (2) the second argument is equivalent to
the first argument of the enclosing method.
When possible, omit the arguments to super to make the code more concise
and maintainable.
## Example
```
class A:
    def foo(self):
        pass
class B(A):
    def bar(self):
        super(B, self).foo()
```
## Use instead:
```
class A:
    def foo(self):
        pass
class B(A):
    def bar(self):
        super().foo()
```