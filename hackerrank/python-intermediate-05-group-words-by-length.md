# Group Words by Length

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Dictionaries of lists
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line of words. Group the words by length. Print one line per length, shortest first, with the words in their original order.

## Input format

One line of space-separated words.

## Output format

One line per length: `length: word word ...`.

## Sample input

```text
a bb cc ddd
```

## Sample output

```text
1: a
2: bb cc
3: ddd
```

## Solution

```python
from collections import defaultdict

groups = defaultdict(list)
for word in input().split():
    groups[len(word)].append(word)
for length in sorted(groups):
    print(f"{length}: {' '.join(groups[length])}")
```

## Explanation

- `defaultdict(list)` creates an empty list the first time a key is used.
- Iterating over `sorted(groups)` gives the lengths in order.
