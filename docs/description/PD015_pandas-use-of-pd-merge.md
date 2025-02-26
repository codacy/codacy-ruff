# pandas-use-of-pd-merge (PD015)
Derived from the pandas-vet linter.
## What it does
Checks for uses of pd.merge on Pandas objects.
## Why is this bad?
In Pandas, the .merge method (exposed on, e.g., DataFrame objects) and
the pd.merge function (exposed on the Pandas module) are equivalent.
For consistency, prefer calling .merge on an object over calling
pd.merge on the Pandas module, as the former is more idiomatic.
Further, pd.merge is not a method, but a function, which prohibits it
from being used in method chains, a common pattern in Pandas code.
## Example
```
import pandas as pd
cats_df = pd.read_csv("cats.csv")
dogs_df = pd.read_csv("dogs.csv")
rabbits_df = pd.read_csv("rabbits.csv")
pets_df = pd.merge(pd.merge(cats_df, dogs_df), rabbits_df)  # Hard to read.
```
## Use instead:
```
import pandas as pd
cats_df = pd.read_csv("cats.csv")
dogs_df = pd.read_csv("dogs.csv")
rabbits_df = pd.read_csv("rabbits.csv")
pets_df = cats_df.merge(dogs_df).merge(rabbits_df)
```