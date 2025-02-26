# custom-type-var-for-self (PYI019)
Derived from the flake8-pyi linter.
Fix is sometimes available.
## What it does
Checks for methods that use custom TypeVars in their
annotations when they could use Self instead.
## Why is this bad?
While the semantics are often identical, using Self is more intuitive
and succinct (per PEP 673) than a custom TypeVar. For example, the
use of Self will typically allow for the omission of type parameters
on the self and cls arguments.
This check currently applies to instance methods that return self,
class methods that return an instance of cls, class methods that return
cls, and __new__ methods.
## Example
```
from typing import TypeVar
_S = TypeVar("_S", bound="Foo")
class Foo:
    def __new__(cls: type[_S], *args: str, **kwargs: int) -> _S: ...
    def foo(self: _S, arg: bytes) -> _S: ...
    @classmethod
    def bar(cls: type[_S], arg: int) -> _S: ...
```
## Use instead:
```
from typing import Self
class Foo:
    def __new__(cls, *args: str, **kwargs: int) -> Self: ...
    def foo(self, arg: bytes) -> Self: ...
    @classmethod
    def bar(cls, arg: int) -> Self: ...
Fix behaviour and safety
The fix replaces all references to the custom type variable in the method's header and body
with references to Self. The fix also adds an import of Self if neither Self nor typing
is already imported in the module. If your target-version setting is set to Python 3.11 or
newer, the fix imports Self from the standard-library typing module; otherwise, the fix
imports Self from the third-party typing_extensions backport package.
If the custom type variable is a [PEP-695]-style TypeVar, the fix also removes the TypeVar
declaration from the method's type parameter list. However, if the type variable is an
old-style TypeVar, the declaration of the type variable will not be removed by this rule's
fix, as the type variable could still be used by other functions, methods or classes. See
unused-private-type-var for a rule that will clean up unused private type
variables.
The fix is only marked as unsafe if there is the possibility that it might delete a comment
from your code.
Preview-mode behaviour
This rule's behaviour has several differences when preview mode is enabled:
The fix for this rule is currently only available if preview mode is enabled.
By default, this rule is only applied to methods that have return-type annotations,
    and the range of the diagnostic is the range of the return-type annotation.
    In preview mode, this rule is also applied to some methods that do not have
    return-type annotations. The range of the diagnostic is the range of the function
    header (from the end of the function name to the end of the parameters).
In preview mode, the rule uses different logic to determine whether an annotation
    refers to a type variable. The preview-mode logic is more accurate, but may lead
    to more methods being flagged than if preview mode is disabled.
```