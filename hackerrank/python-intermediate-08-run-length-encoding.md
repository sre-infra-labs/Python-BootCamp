# Run-Length Encoding

- **Language:** Python
- **Level:** Intermediate
- **Topic:** itertools.groupby
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a string. Compress each run of equal characters into the character followed by the run length. For example `aaabbc` becomes `a3b2c1`.

## Input format

One line of letters.

## Output format

The encoded string.

## Sample input

```text
aaabbc
```

## Sample output

```text
a3b2c1
```

## Solution

```python
from itertools import groupby

s = input().strip()
print("".join(f"{ch}{len(list(group))}" for ch, group in groupby(s)))
```

## Explanation

- `groupby` groups consecutive equal items, which is exactly what run-length encoding needs.
