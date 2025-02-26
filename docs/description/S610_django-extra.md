# django-extra (S610)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of Django's extra function where one or more arguments
passed are not literal expressions.
## Why is this bad?
Django's extra function can be used to execute arbitrary SQL queries,
which can in turn lead to SQL injection vulnerabilities.
## Example
```
from django.contrib.auth.models import User
# String interpolation creates a security loophole that could be used
# for SQL injection:
User.objects.all().extra(select={"test": "%secure" % "nos"})
```
## Use instead:
```
from django.contrib.auth.models import User
# SQL injection is impossible if all arguments are literal expressions:
User.objects.all().extra(select={"test": "secure"})
```