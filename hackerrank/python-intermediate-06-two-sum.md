# Two Sum

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Hash maps
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n`, a list of integers, then a target. Print the indices `i j` (with `i < j`) of the first pair whose values add up to the target. Print `-1 -1` if there is no such pair.

## Input format

Line 1: `n`. Line 2: `n` integers. Line 3: the target.

## Output format

Two indices separated by a space.

## Sample input

```text
4
2 7 11 15
9
```

## Sample output

```text
0 1
```

## Solution

```python
n = int(input())
nums = list(map(int, input().split()))
target = int(input())
seen = {}
for j, x in enumerate(nums):
    if target - x in seen:
        print(seen[target - x], j)
        break
    seen[x] = j
else:
    print(-1, -1)
```

## Explanation

- The dictionary maps each value to its index, so each lookup for the complement is O(1).
- `for ... else` runs only when the loop finishes without `break`.
