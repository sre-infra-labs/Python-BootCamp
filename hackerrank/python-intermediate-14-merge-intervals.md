# Merge Overlapping Intervals

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Sorting and merging
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` intervals as `start end`. Merge the intervals that overlap or touch, and print the merged intervals in order.

## Input format

Line 1: `n`. Then `n` lines `start end`.

## Output format

One merged interval per line.

## Sample input

```text
4
1 3
2 6
8 10
15 18
```

## Sample output

```text
1 6
8 10
15 18
```

## Solution

```python
n = int(input())
intervals = sorted(tuple(map(int, input().split())) for _ in range(n))
merged = []
for start, end in intervals:
    if merged and start <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])
for start, end in merged:
    print(start, end)
```

## Explanation

- Sorting by start means an interval can only overlap the one just before it in the merged list.
