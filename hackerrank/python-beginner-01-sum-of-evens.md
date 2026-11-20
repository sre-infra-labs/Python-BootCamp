# Sum of Even Numbers

- **Language:** Python
- **Level:** Beginner
- **Topic:** Lists and loops
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a list of integers and print the sum of the even ones.

## Input format

The first line has `n`. The second line has `n` space-separated integers.

## Output format

One line: the sum of the even integers.

## Sample input

```text
5
1 2 3 4 5
```

## Sample output

```text
6
```

## Solution

```python
n = int(input())
nums = list(map(int, input().split()))
print(sum(x for x in nums if x % 2 == 0))
```

## Explanation

- `x % 2 == 0` tests for an even number.
- A generator expression feeds `sum` without building a new list.
