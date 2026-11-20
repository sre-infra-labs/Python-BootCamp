# Largest Minus Smallest

- **Language:** Python
- **Level:** Beginner
- **Topic:** Lists and built-ins
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line of integers and print the largest value minus the smallest value.

## Input format

One line of space-separated integers.

## Output format

One integer.

## Sample input

```text
4 9 1 7
```

## Sample output

```text
8
```

## Solution

```python
nums = list(map(int, input().split()))
print(max(nums) - min(nums))
```

## Explanation

- `max` and `min` each scan the list once.
