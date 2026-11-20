# Distinct Permutations

- **Language:** Python
- **Level:** Advanced
- **Topic:** itertools
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a string of up to 6 lowercase letters. Print every distinct permutation once, in sorted order, one per line.

## Input format

One line with the string.

## Output format

One permutation per line.

## Sample input

```text
aab
```

## Sample output

```text
aab
aba
baa
```

## Solution

```python
from itertools import permutations

s = input().strip()
for p in sorted(set("".join(t) for t in permutations(s))):
    print(p)
```

## Explanation

- `permutations` produces duplicates when letters repeat, so a `set` removes them.
- Sorting the set gives the required order.
