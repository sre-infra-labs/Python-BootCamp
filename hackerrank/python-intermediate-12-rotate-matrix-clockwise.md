# Rotate a Square Matrix

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Matrix indexing
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read an `n` by `n` matrix and print it rotated 90 degrees clockwise.

## Input format

Line 1: `n`. Then `n` lines of `n` integers.

## Output format

`n` lines of values.

## Sample input

```text
2
1 2
3 4
```

## Sample output

```text
3 1
4 2
```

## Solution

```python
n = int(input())
m = [input().split() for _ in range(n)]
rotated = [[m[n - 1 - j][i] for j in range(n)] for i in range(n)]
for row in rotated:
    print(" ".join(row))
```

## Explanation

- The value at row `i`, column `j` of the result comes from row `n-1-j`, column `i` of the input.
