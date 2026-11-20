# Union, Intersection and Difference

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Sets
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read two lines of integers, A and B. Print the size of the union. Then print the sorted intersection. Then print the sorted values in A that are not in B.

## Input format

Two lines of space-separated integers.

## Output format

Three lines: union size, intersection, A minus B.

## Sample input

```text
1 2 3 4
3 4 5
```

## Sample output

```text
5
3 4
1 2
```

## Solution

```python
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a | b))
print(" ".join(map(str, sorted(a & b))))
print(" ".join(map(str, sorted(a - b))))
```

## Explanation

- `|` is union, `&` is intersection and `-` is difference.
