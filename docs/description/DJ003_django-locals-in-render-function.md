# django-locals-in-render-function (DJ003)
Derived from the flake8-django linter.
## What it does
Checks for the use of locals() in render functions.
## Why is this bad?
Using locals() can expose internal variables or other unintentional
data to the rendered template.
## Example
```
from django.shortcuts import render
def index(request):
    posts = Post.objects.all()
    return render(request, "app/index.html", locals())
```
## Use instead:
```
from django.shortcuts import render
def index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "app/index.html", context)
```