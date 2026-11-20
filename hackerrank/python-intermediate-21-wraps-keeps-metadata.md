# Keep Function Metadata with wraps

- **Language:** Python
- **Level:** Intermediate
- **Topic:** functools.wraps
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read two integers `w h`. Decorate `area` with a pass-through decorator that uses `functools.wraps`. Print the function name, its docstring, and the area, separated by spaces.

## Input format

One line: `w h`.

## Output format

One line: `name docstring area`.

## Sample input

```text
3 4
```

## Sample output

```text
area Rectangle area. 12
```

## Solution

```python
import functools


def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@logged
def area(w, h):
    """Rectangle area."""
    return w * h


print(area.__name__, area.__doc__, area(*map(int, input().split())))
```

## Explanation

- Without `functools.wraps`, `area.__name__` would be `wrapper` and the docstring would be lost.
