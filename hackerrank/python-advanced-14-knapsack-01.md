# 0/1 Knapsack

- **Language:** Python
- **Level:** Advanced
- **Topic:** Dynamic programming
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` items and a capacity `W`. Each item has a weight and a value, and each can be used at most once. Print the largest total value that fits in capacity `W`.

## Input format

Line 1: `n W`. Then `n` lines `weight value`.

## Output format

One integer.

## Sample input

```text
3 5
2 3
3 4
4 5
```

## Sample output

```text
7
```

## Solution

```python
n, W = map(int, input().split())
best = [0] * (W + 1)  # best[c] = max value using capacity c
for _ in range(n):
    weight, value = map(int, input().split())
    for cap in range(W, weight - 1, -1):  # backwards, so each item is used once
        best[cap] = max(best[cap], best[cap - weight] + value)
print(best[W])
```

## Explanation

- Looping the capacity downwards stops an item from being counted twice in the same row.
