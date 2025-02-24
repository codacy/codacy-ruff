# django-unordered-body-content-in-model (DJ012)
Derived from the flake8-django linter.
## What it does
Checks for the order of Model's inner classes, methods, and fields as per
the Django Style Guide.
## Why is this bad?
The Django Style Guide specifies that the order of Model inner classes,
attributes and methods should be as follows:
All database fields
Custom manager attributes
class Meta
def __str__()
def save()
def get_absolute_url()
Any custom methods
## Examples
```
from django.db import models
class StrBeforeFieldModel(models.Model):
    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"
    def __str__(self):
        return "foobar"
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=40)
```
## Use instead:
```
from django.db import models
class StrBeforeFieldModel(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=40)
    class Meta:
        verbose_name = "test"
        verbose_name_plural = "tests"
    def __str__(self):
        return "foobar"
```