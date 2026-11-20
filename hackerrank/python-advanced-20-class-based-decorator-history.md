# Class-Based Decorator that Records History

- **Language:** Python
- **Level:** Advanced
- **Topic:** Class-based decorators
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a class `Traced` that wraps a function and records every call as `(args, result)` in a list called `history`. Read integers on one line, call `double` on each, then print the number of recorded calls and the last record.

## Input format

One line of integers.

## Output format

One line: `count last_record`.

## Sample input

```text
1 2 3
```

## Sample output

```text
3 ((3,), 6)
```

## Solution

```python
import functools


class Traced:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.history = []

    def __call__(self, *args):
        result = self.func(*args)
        self.history.append((args, result))
        return result


@Traced
def double(x):
    return 2 * x


for value in map(int, input().split()):
    double(value)
print(len(double.history), double.history[-1])
```

## Explanation

- A class can be a decorator when it defines `__call__`. Its state lives on the instance.
- `update_wrapper` copies the name and docstring onto the instance.
