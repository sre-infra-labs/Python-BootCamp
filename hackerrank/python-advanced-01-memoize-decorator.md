# Stair Climbing with a Memoize Decorator

- **Language:** Python
- **Level:** Advanced
- **Topic:** Decorators and recursion
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a `memoize` decorator that caches results. Use it on a function that counts the ways to climb `n` stairs taking one or two steps at a time. Read `n` and print the count.

## Input format

One integer `n` (0 to 500).

## Output format

One integer: the number of ways.

## Sample input

```text
5
```

## Sample output

```text
8
```

## Solution

```python
def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@memoize
def ways(n):
    if n <= 1:
        return 1
    return ways(n - 1) + ways(n - 2)


print(ways(int(input())))
```

## Explanation

- Without the cache, the same subproblems are solved again and again, which is exponential.
- The decorator stores each result, so each `n` is computed once. Recursion depth is limited, so very large `n` needs an iterative version.
