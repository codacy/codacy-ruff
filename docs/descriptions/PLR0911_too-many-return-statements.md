# too-many-return-statements (PLR0911)
Derived from the Pylint linter.
## What it does
Checks for functions or methods with too many return statements.
By default, this rule allows up to six return statements, as configured by
the lint.pylint.max-returns option.
## Why is this bad?
Functions or methods with many return statements are harder to understand
and maintain, and often indicative of complex logic.
## Example
```
def capital(country: str) -> str | None:
    if country == "England":
        return "London"
    elif country == "France":
        return "Paris"
    elif country == "Poland":
        return "Warsaw"
    elif country == "Romania":
        return "Bucharest"
    elif country == "Spain":
        return "Madrid"
    elif country == "Thailand":
        return "Bangkok"
    else:
        return None
```
## Use instead:
```
def capital(country: str) -> str | None:
    capitals = {
        "England": "London",
        "France": "Paris",
        "Poland": "Warsaw",
        "Romania": "Bucharest",
        "Spain": "Madrid",
        "Thailand": "Bangkok",
    }
    return capitals.get(country)
```