# Edit Distance

- **Language:** Python
- **Level:** Advanced
- **Topic:** Dynamic programming on strings
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read two words. Print the minimum number of single-character insertions, deletions and substitutions that turn the first word into the second.

## Input format

Two lines, each a word.

## Output format

One integer.

## Sample input

```text
kitten
sitting
```

## Sample output

```text
3
```

## Solution

```python
a = input().strip()
b = input().strip()
prev = list(range(len(b) + 1))
for i, ca in enumerate(a, 1):
    cur = [i]
    for j, cb in enumerate(b, 1):
        cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
    prev = cur
print(prev[-1])
```

## Explanation

- Only the previous row of the table is kept, so memory is `O(len(b))`.
