# django-all-with-model-form (DJ007)
Derived from the flake8-django linter.
## What it does
Checks for the use of fields = "__all__" in Django ModelForm
classes.
## Why is this bad?
If a ModelForm includes the fields = "__all__" attribute, any new
field that is added to the model will automatically be exposed for
modification.
## Example
```
from django.forms import ModelForm
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
```
## Use instead:
```
from django.forms import ModelForm
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
```