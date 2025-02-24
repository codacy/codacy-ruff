# sorted-min-max (FURB192)
Derived from the refurb linter.
Fix is sometimes available.
This rule is unstable and in preview. The --preview flag is required for use.
## What it does
Checks for uses of sorted() to retrieve the minimum or maximum value in
a sequence.
## Why is this bad?
Using sorted() to compute the minimum or maximum value in a sequence is
inefficient and less readable than using min() or max() directly.
## Example
```
nums = [3, 1, 4, 1, 5]
lowest = sorted(nums)[0]
highest = sorted(nums)[-1]
highest = sorted(nums, reverse=True)[0]
```
## Use instead:
```
nums = [3, 1, 4, 1, 5]
lowest = min(nums)
highest = max(nums)
Fix safety
In some cases, migrating to min or max can lead to a change in behavior,
notably when breaking ties.
As an example, sorted(data, key=itemgetter(0), reverse=True)[0] will return
the last "minimum" element in the list, if there are multiple elements with
the same key. However, min(data, key=itemgetter(0)) will return the first
"minimum" element in the list in the same scenario.
As such, this rule's fix is marked as unsafe when the reverse keyword is used.
```