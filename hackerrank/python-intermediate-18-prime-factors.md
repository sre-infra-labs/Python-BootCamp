# Prime Factorisation

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Number theory
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a positive integer greater than 1. Print its prime factors in ascending order, repeated as many times as they divide the number, separated by spaces.

## Input format

One integer.

## Output format

One line of factors.

## Sample input

```text
360
```

## Sample output

```text
2 2 2 3 3 5
```

## Solution

```python
n = int(input())
factors = []
d = 2
while d * d <= n:
    while n % d == 0:
        factors.append(d)
        n //= d
    d += 1
if n > 1:
    factors.append(n)
print(" ".join(map(str, factors)))
```

## Explanation

- Trial division only needs to go up to the square root of what remains.
- Whatever is left above 1 after the loop is itself prime.
