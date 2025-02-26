# suspicious-eval-usage (S307)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of the builtin eval() function.
## Why is this bad?
The eval() function is insecure as it enables arbitrary code execution.
If you need to evaluate an expression from a string, consider using
ast.literal_eval() instead, which will raise an exception if the
expression is not a valid Python literal.
In preview, this rule will also flag references to eval.
## Example
```
x = eval(input("Enter a number: "))
```
## Use instead:
```
from ast import literal_eval
x = literal_eval(input("Enter a number: "))
```