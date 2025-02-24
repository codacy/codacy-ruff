# missing-f-string-syntax (RUF027)
Fix is always available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Searches for strings that look like they were meant to be f-strings, but are missing an f prefix.
## Why is this bad?
Expressions inside curly braces are only evaluated if the string has an f prefix.
Details
There are many possible string literals which are not meant to be f-strings
despite containing f-string-like syntax. As such, this lint ignores all strings
where one of the following conditions applies:
The string is a standalone expression. For example, the rule ignores all docstrings.
The string is part of a function call with argument names that match at least one variable
    (for example: format("Message: {value}", value="Hello World"))
The string (or a parent expression of the string) has a direct method call on it
    (for example: "{value}".format(...))
The string has no {...} expression sections, or uses invalid f-string syntax.
The string references variables that are not in scope, or it doesn't capture variables at all.
Any format specifiers in the potential f-string are invalid.
The string is part of a function call that is known to expect a template string rather than an
    evaluated f-string: for example, a logging call, a gettext call,
    or a FastAPI path.
## Example
```
name = "Sarah"
day_of_week = "Tuesday"
print("Hello {name}! It is {day_of_week} today!")
```
## Use instead:
```
name = "Sarah"
day_of_week = "Tuesday"
print(f"Hello {name}! It is {day_of_week} today!")
```