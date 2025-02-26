# fast-api-redundant-response-model (FAST001)
Derived from the FastAPI linter.
Fix is always available.
## What it does
Checks for FastAPI routes that use the optional response_model parameter
with the same type as the return type.
## Why is this bad?
FastAPI routes automatically infer the response model type from the return
type, so specifying it explicitly is redundant.
The response_model parameter is used to override the default response
model type. For example, response_model can be used to specify that
a non-serializable response type should instead be serialized via an
alternative type.
For more information, see the FastAPI documentation.
## Example
```
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name: str
@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    return item
```
## Use instead:
```
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Item(BaseModel):
    name: str
@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item
```