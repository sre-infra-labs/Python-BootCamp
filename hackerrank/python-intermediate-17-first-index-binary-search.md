# First Index of a Value

- **Language:** Python
- **Level:** Intermediate
- **Topic:** bisect
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a sorted list of `n` integers and `q` queries. For each query value, print the index of its first occurrence, or -1 if it is not in the list.

## Input format

Line 1: `n`. Line 2: the sorted values. Line 3: `q`. Then `q` query values, one per line.

## Output format

One line per query.

## Sample input

```text
5
1 3 3 5 8
3
3
4
8
```

## Sample output

```text
1
-1
4
```

## Solution

```python
from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    x = int(input())
    i = bisect_left(nums, x)
    print(i if i < n and nums[i] == x else -1)
```

## Explanation

- `bisect_left` returns the first position where the value could go, so it is the first occurrence if the value exists.
