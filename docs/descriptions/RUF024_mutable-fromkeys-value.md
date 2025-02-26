# mutable-fromkeys-value (RUF024)
Fix is sometimes available.
## What it does
Checks for mutable objects passed as a value argument to dict.fromkeys.
## Why is this bad?
All values in the dictionary created by the dict.fromkeys method
refer to the same instance of the provided object. If that object is
modified, all values are modified, which can lead to unexpected behavior.
For example, if the empty list ([]) is provided as the default value,
all values in the dictionary will use the same list; as such, appending to
any one entry will append to all entries.
Instead, use a comprehension to generate a dictionary with distinct
instances of the default value.
## Example
```
cities = dict.fromkeys(["UK", "Poland"], [])
cities["UK"].append("London")
cities["Poland"].append("Poznan")
print(cities)  # {'UK': ['London', 'Poznan'], 'Poland': ['London', 'Poznan']}
```
## Use instead:
```
cities = {country: [] for country in ["UK", "Poland"]}
cities["UK"].append("London")
cities["Poland"].append("Poznan")
print(cities)  # {'UK': ['London'], 'Poland': ['Poznan']}
Fix safety
This rule's fix is marked as unsafe, as the edit will change the behavior of
the program by using a distinct object for every value in the dictionary,
rather than a shared mutable instance. In some cases, programs may rely on
the previous behavior.
```