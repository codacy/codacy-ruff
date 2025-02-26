# django-exclude-with-model-form (DJ006)
Derived from the flake8-django linter.
## What it does
Checks for the use of exclude in Django ModelForm classes.
## Why is this bad?
If a ModelForm includes the exclude attribute, any new field that
is added to the model will automatically be exposed for modification.
## Example
```
from django.forms import ModelForm
class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ["author"]
```
## Use instead:
```
from django.forms import ModelForm
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
```