# Longest Run of Ones

- **Language:** Python
- **Level:** Beginner
- **Topic:** Loops and counters
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a string of 0s and 1s. Print the length of the longest run of consecutive 1s.

## Input format

One binary string.

## Output format

One integer.

## Sample input

```text
110111011
```

## Sample output

```text
3
```

## Solution

```python
s = input().strip()
best = current = 0
for ch in s:
    current = current + 1 if ch == "1" else 0
    best = max(best, current)
print(best)
```

## Explanation

- `current` resets to 0 at each 0, and `best` keeps the largest value seen.
