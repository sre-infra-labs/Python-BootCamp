# Length of the Longest Increasing Subsequence

- **Language:** Python
- **Level:** Advanced
- **Topic:** Dynamic programming
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a list of integers and print the length of its longest strictly increasing subsequence. The subsequence does not need to be contiguous. Aim for `O(n log n)`.

## Input format

Line 1: `n`. Line 2: `n` integers.

## Output format

One integer: the length of the longest strictly increasing subsequence.

## Sample input

```text
6
10 9 2 5 3 7
```

## Sample output

```text
3
```

## Solution

```python
from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))
tails = []  # tails[i] = smallest tail of an increasing subsequence of length i+1
for x in nums:
    i = bisect_left(tails, x)
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x
print(len(tails))
```

## Explanation

- `tails` is not the subsequence itself, only its length is correct at the end.
- `bisect_left` finds where `x` fits, so each value costs `O(log n)`, giving `O(n log n)` overall.
