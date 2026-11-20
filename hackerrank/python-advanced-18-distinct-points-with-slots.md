# Distinct Points

- **Language:** Python
- **Level:** Advanced
- **Topic:** Classes and hashing
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` points as `x y`. Define a `Point` class with `__slots__`, `__eq__` and `__hash__` so that equal coordinates count as the same point. Print the number of distinct points.

## Input format

Line 1: `n`. Then `n` lines `x y`.

## Output format

One integer.

## Sample input

```text
4
1 2
3 4
1 2
0 0
```

## Sample output

```text
3
```

## Solution

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))


n = int(input())
points = {Point(*map(int, input().split())) for _ in range(n)}
print(len(points))
```

## Explanation

- `__slots__` stops each instance from creating a `__dict__`, which saves memory.
- A set uses `__hash__` and `__eq__` together, so duplicates collapse.
