# docstring-extraneous-returns (DOC202)
Derived from the pydoclint linter.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for function docstrings with unnecessary "Returns" sections.
## Why is this bad?
A function without an explicit return statement should not have a
"Returns" section in its docstring.
This rule is not enforced for abstract methods. It is also ignored for
"stub functions": functions where the body only consists of pass, ...,
raise NotImplementedError, or similar.
## Example
```
def say_hello(n: int) -> None:
    """Says hello to the user.
    Args:
        n: Number of times to say hello.
    Returns:
        Doesn't return anything.
    """
    for _ in range(n):
        print("Hello!")
```
## Use instead:
```
def say_hello(n: int) -> None:
    """Says hello to the user.
    Args:
        n: Number of times to say hello.
    """
    for _ in range(n):
        print("Hello!")
```