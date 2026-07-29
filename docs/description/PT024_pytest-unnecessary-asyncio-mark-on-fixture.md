# pytest-unnecessary-asyncio-mark-on-fixture (PT024)
Added in v0.0.208 ·
Related issues ·
View source
Derived from the flake8-pytest-style linter.
Fix is always available.
## What it does
Checks for unnecessary @pytest.mark.asyncio decorators applied to fixtures.
## Why is this bad?
pytest.mark.asyncio is unnecessary for fixtures.
## Example
```
import pytest
@pytest.mark.asyncio()
@pytest.fixture()
async def my_fixture():
    return 0
```
## Use instead:
```
import pytest
@pytest.fixture()
async def my_fixture():
    return 0
```