# Spiral Order of a Matrix

- **Language:** Python
- **Level:** Advanced
- **Topic:** 2D arrays
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read an `r` by `c` matrix. Print its values in spiral order, starting at the top-left and moving clockwise, separated by spaces.

## Input format

Line 1: `r c`. Then `r` lines with `c` integers.

## Output format

One line with the values in spiral order.

## Sample input

```text
3 3
1 2 3
4 5 6
7 8 9
```

## Sample output

```text
1 2 3 6 9 8 7 4 5
```

## Solution

```python
r, c = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(r)]
top, bottom, left, right = 0, r - 1, 0, c - 1
out = []
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        out.append(m[top][j])
    top += 1
    for i in range(top, bottom + 1):
        out.append(m[i][right])
    right -= 1
    if top <= bottom:
        for j in range(right, left - 1, -1):
            out.append(m[bottom][j])
        bottom -= 1
    if left <= right and top <= bottom:
        for i in range(bottom, top - 1, -1):
            out.append(m[i][left])
        left += 1
print(" ".join(map(str, out)))
```

## Explanation

- Four boundaries (top, bottom, left, right) shrink after each side is read.
- The checks before the last two sides stop a single row or column from being read twice.
