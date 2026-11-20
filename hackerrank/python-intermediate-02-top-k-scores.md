# Top K Scores

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Sorting with keys
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` and `k`, then `n` lines each with a name and a score. Print the `k` best entries. Sort by score, highest first. Break ties by name, alphabetically.

## Input format

First line: `n k`. Then `n` lines: `name score`.

## Output format

`k` lines: `name score`, in the sorted order.

## Sample input

```text
4 2
alice 88
bob 95
carol 88
dan 70
```

## Sample output

```text
bob 95
alice 88
```

## Solution

```python
n, k = map(int, input().split())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
rows.sort(key=lambda r: (-r[1], r[0]))
for name, score in rows[:k]:
    print(name, score)
```

## Explanation

- `key=lambda r: (-r[1], r[0])` sorts by score descending, then name ascending.
- Negating the score avoids needing `reverse=True`, which would also reverse the name order.
