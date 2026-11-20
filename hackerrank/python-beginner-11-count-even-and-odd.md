# Count Even and Odd Numbers

- **Language:** Python
- **Level:** Beginner
- **Topic:** Counting
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` and `n` integers. Print the count of even numbers and the count of odd numbers, separated by a space.

## Input format

Line 1: `n`. Line 2: `n` integers.

## Output format

One line: `even odd`.

## Sample input

```text
5
1 2 3 4 6
```

## Sample output

```text
3 2
```

## Solution

```python
n = int(input())
nums = list(map(int, input().split()))
even = sum(1 for x in nums if x % 2 == 0)
print(even, len(nums) - even)
```

## Explanation

- Count the evens once, then the odds are the rest of the list.
