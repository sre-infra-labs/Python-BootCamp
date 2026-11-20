# K-th Smallest Value

- **Language:** Python
- **Level:** Advanced
- **Topic:** heapq
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` and `k`, then `n` integers. Print the k-th smallest value (with duplicates counted).

## Input format

Line 1: `n k`. Line 2: `n` integers.

## Output format

One integer.

## Sample input

```text
6 3
7 10 4 3 20 15
```

## Sample output

```text
7
```

## Solution

```python
import heapq

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(heapq.nsmallest(k, nums)[-1])
```

## Explanation

- `nsmallest` returns the k smallest values in order, so the last one is the answer.
- For very large inputs a bounded heap of size k keeps memory small.
