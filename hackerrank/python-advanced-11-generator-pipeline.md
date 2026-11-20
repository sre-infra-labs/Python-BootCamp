# Generator Pipeline

- **Language:** Python
- **Level:** Advanced
- **Topic:** Generator pipelines
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line of integers. Build a lazy pipeline that keeps only the odd values, squares them, and sums the results. Print the sum.

## Input format

One line of integers.

## Output format

One integer.

## Sample input

```text
1 2 3 4 5
```

## Sample output

```text
35
```

## Solution

```python
def only_odd(values):
    for v in values:
        if v % 2:
            yield v


def squared(values):
    for v in values:
        yield v * v


nums = map(int, input().split())
print(sum(squared(only_odd(nums))))
```

## Explanation

- Each stage pulls one value at a time, so no intermediate lists are built.
