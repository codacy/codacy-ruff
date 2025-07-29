# fast-api-non-annotated-dependency (FAST002)
Derived from the FastAPI linter.
Fix is sometimes available.
## What it does
Identifies FastAPI routes with deprecated uses of Depends or similar.
## Why is this bad?
The FastAPI documentation recommends the use of typing.Annotated
for defining route dependencies and parameters, rather than using Depends,
Query or similar as a default value for a parameter. Using this approach
everywhere helps ensure consistency and clarity in defining dependencies
and parameters.
Annotated was added to the typing module in Python 3.9; however,
the third-party typing_extensions package
provides a backport that can be used on older versions of Python.
## Example
```
from fastapi import Depends, FastAPI
app = FastAPI()
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons
```
## Use instead:
```
from typing import Annotated
from fastapi import Depends, FastAPI
app = FastAPI()
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
@app.get("/items/")
async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
    return commons
Fix safety
This fix is always unsafe, as adding/removing/changing a function parameter's
default value can change runtime behavior. Additionally, comments inside the
deprecated uses might be removed.
Availability
Because this rule relies on the third-party typing_extensions module for Python versions
before 3.9, if the target version is < 3.9 and typing_extensions imports have been
disabled by the lint.typing-extensions linter option the diagnostic will not be emitted
and no fix will be offered.
```