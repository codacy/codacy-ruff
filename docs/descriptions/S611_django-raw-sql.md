# django-raw-sql (S611)
Derived from the flake8-bandit linter.
## What it does
Checks for uses of Django's RawSQL function.
## Why is this bad?
Django's RawSQL function can be used to execute arbitrary SQL queries,
which can in turn lead to SQL injection vulnerabilities.
## Example
```
from django.db.models.expressions import RawSQL
from django.contrib.auth.models import User
User.objects.annotate(val=("%secure" % "nos", []))
```