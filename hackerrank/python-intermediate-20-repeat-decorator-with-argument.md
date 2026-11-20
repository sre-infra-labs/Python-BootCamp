# Repeat Decorator with an Argument

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Decorator factories
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a decorator factory `repeat(times)`. The decorated function returns a list of its result repeated `times` times. Read a word and print the list joined by spaces, using `@repeat(3)`.

## Input format

One word.

## Output format

The word three times, separated by spaces.

## Sample input

```text
ok
```

## Sample output

```text
OK OK OK
```

## Solution

```python
import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator


@repeat(3)
def shout(word):
    return word.upper()


print(" ".join(shout(input().strip())))
```

## Explanation

- A decorator with arguments needs one extra level: the factory returns the decorator, which returns the wrapper.
