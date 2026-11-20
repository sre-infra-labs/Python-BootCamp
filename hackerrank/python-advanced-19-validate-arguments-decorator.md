# Validate Arguments with a Decorator

- **Language:** Python
- **Level:** Advanced
- **Topic:** Decorators and validation
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a `positive_args` decorator that raises `ValueError("negative argument")` if any argument is negative. Apply it to `square`. Read one integer and print its square. If the decorator raises, print `invalid: negative argument`.

## Input format

One integer.

## Output format

The square, or the invalid message.

## Sample input

```text
-2
```

## Sample output

```text
invalid: negative argument
```

## Solution

```python
import functools


def positive_args(func):
    @functools.wraps(func)
    def wrapper(*args):
        if any(a < 0 for a in args):
            raise ValueError("negative argument")
        return func(*args)
    return wrapper


@positive_args
def square(x):
    return x * x


try:
    print(square(int(input())))
except ValueError as exc:
    print("invalid:", exc)
```

## Explanation

- Validation happens before the function body runs, so `square` never sees bad input.
- The caller catches the same `ValueError` the decorator raised.
