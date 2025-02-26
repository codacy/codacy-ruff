# pytest-parametrize-values-wrong-type (PT007)
Derived from the flake8-pytest-style linter.
Fix is sometimes available.
## What it does
Checks for the type of parameter values passed to pytest.mark.parametrize.
## Why is this bad?
The argvalues argument of pytest.mark.parametrize takes an iterator of
parameter values, which can be provided as lists or tuples.
To aid in readability, it's recommended to use a consistent style for the
list of values rows, and, in the case of multiple parameters, for each row
of values.
The style for the list of values rows can be configured via the
lint.flake8-pytest-style.parametrize-values-type setting, while the
style for each row of values can be configured via the
lint.flake8-pytest-style.parametrize-values-row-type setting.
For example, lint.flake8-pytest-style.parametrize-values-type will lead to
the following expectations:
tuple: @pytest.mark.parametrize("value", ("a", "b", "c"))
list: @pytest.mark.parametrize("value", ["a", "b", "c"])
Similarly, lint.flake8-pytest-style.parametrize-values-row-type will lead to
the following expectations:
tuple: @pytest.mark.parametrize(("key", "value"), [("a", "b"), ("c", "d")])
list: @pytest.mark.parametrize(("key", "value"), [["a", "b"], ["c", "d"]])
## Example
```
import pytest
# expected list, got tuple
@pytest.mark.parametrize("param", (1, 2))
def test_foo(param): ...
# expected top-level list, got tuple
@pytest.mark.parametrize(
    ("param1", "param2"),
    (
        (1, 2),
        (3, 4),
    ),
)
def test_bar(param1, param2): ...
# expected individual rows to be tuples, got lists
@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        [1, 2],
        [3, 4],
    ],
)
def test_baz(param1, param2): ...
```
## Use instead:
```
import pytest
@pytest.mark.parametrize("param", [1, 2, 3])
def test_foo(param): ...
@pytest.mark.parametrize(("param1", "param2"), [(1, 2), (3, 4)])
def test_bar(param1, param2): ...
```