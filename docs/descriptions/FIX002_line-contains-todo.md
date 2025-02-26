# line-contains-todo (FIX002)
Derived from the flake8-fixme linter.
## What it does
Checks for "TODO" comments.
## Why is this bad?
"TODO" comments are used to describe an issue that should be resolved
(usually, a missing feature, optimization, or refactoring opportunity).
Consider resolving the issue before deploying the code.
Note that if you use "TODO" comments as a form of documentation (e.g.,
to provide context for future work),
this rule may not be appropriate for your project.
## Example
```
def greet(name):
    return f"Hello, {name}!"  # TODO: Add support for custom greetings.
```