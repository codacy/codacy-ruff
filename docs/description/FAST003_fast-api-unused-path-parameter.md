# fast-api-unused-path-parameter (FAST003)
Derived from the FastAPI linter.
Fix is sometimes available.
## What it does
Identifies FastAPI routes that declare path parameters in the route path
that are not included in the function signature.
## Why is this bad?
Path parameters are used to extract values from the URL path.
If a path parameter is declared in the route path but not in the function
signature, it will not be accessible in the function body, which is likely
a mistake.
If a path parameter is declared in the route path, but as a positional-only
argument in the function signature, it will also not be accessible in the
function body, as FastAPI will not inject the parameter.
Known problems
If the path parameter is not a valid Python identifier (e.g., user-id, as
opposed to user_id), FastAPI will normalize it. However, this rule simply
ignores such path parameters, as FastAPI's normalization behavior is undocumented.
## Example
```
from fastapi import FastAPI
app = FastAPI()
@app.get("/things/{thing_id}")
async def read_thing(query: str): ...
```
## Use instead:
```
from fastapi import FastAPI
app = FastAPI()
@app.get("/things/{thing_id}")
async def read_thing(thing_id: int, query: str): ...
Fix safety
This rule's fix is marked as unsafe, as modifying a function signature can
change the behavior of the code.
```