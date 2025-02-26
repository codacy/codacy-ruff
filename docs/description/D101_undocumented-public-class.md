# undocumented-public-class (D101)
Derived from the pydocstyle linter.
## What it does
Checks for undocumented public class definitions.
## Why is this bad?
Public classes should be documented via docstrings to outline their purpose
and behavior.
Generally, a class docstring should describe the class's purpose and list
its public attributes and methods.
If the codebase adheres to a standard format for class docstrings, follow
that format for consistency.
## Example
```
class Player:
    def __init__(self, name: str, points: int = 0) -> None:
        self.name: str = name
        self.points: int = points
    def add_points(self, points: int) -> None:
        self.points += points
Use instead (in the NumPy docstring format):
class Player:
    """A player in the game.
    Attributes
    ----------
    name : str
        The name of the player.
    points : int
        The number of points the player has.
    Methods
    -------
    add_points(points: int) -> None
        Add points to the player's score.
    """
    def __init__(self, name: str, points: int = 0) -> None:
        self.name: str = name
        self.points: int = points
    def add_points(self, points: int) -> None:
        self.points += points
Or (in the Google docstring format):
class Player:
    """A player in the game.
    Attributes:
        name: The name of the player.
        points: The number of points the player has.
    """
    def __init__(self, name: str, points: int = 0) -> None:
        self.name: str = name
        self.points: int = points
    def add_points(self, points: int) -> None:
        self.points += points
```