# unnecessary-paren-on-raise-exception (RSE102)
Derived from the flake8-raise linter.
Fix is always available.
## What it does
Checks for unnecessary parentheses on raised exceptions.
## Why is this bad?
If an exception is raised without any arguments, parentheses are not
required, as the raise statement accepts either an exception instance
or an exception class (which is then implicitly instantiated).
Removing the parentheses makes the code more concise.
Known problems
Parentheses can only be omitted if the exception is a class, as opposed to
a function call. This rule isn't always capable of distinguishing between
the two.
For example, if you import a function module.get_exception from another
module, and module.get_exception returns an exception object, this rule will
incorrectly mark the parentheses in raise module.get_exception() as
unnecessary.
## Example
```
raise TypeError()
```
## Use instead:
```
raise TypeError
```