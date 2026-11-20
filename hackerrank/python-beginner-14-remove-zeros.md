# Remove Zeros from a List

- **Language:** Python
- **Level:** Beginner
- **Topic:** List comprehension
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` and `n` integers. Remove every zero. Print how many values remain, then the remaining values.

## Input format

Line 1: `n`. Line 2: `n` integers.

## Output format

Line 1: the count. Line 2: the values.

## Sample input

```text
5
0 3 0 7 1
```

## Sample output

```text
3
3 7 1
```

## Solution

```python
n = int(input())
nums = [x for x in map(int, input().split()) if x != 0]
print(len(nums))
print(" ".join(map(str, nums)))
```

## Explanation

- The list comprehension keeps only the non-zero values.
