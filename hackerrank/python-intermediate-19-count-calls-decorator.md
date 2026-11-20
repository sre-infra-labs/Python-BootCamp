# Count Calls with a Decorator

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Decorators with state
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a `count_calls` decorator that stores how many times the wrapped function was called in an attribute named `calls`. Read `n`, then `n` names, call `greet` once per name, and print the call count.

## Input format

Line 1: `n`. Then `n` names.

## Output format

One integer.

## Sample input

```text
3
ann
ben
cy
```

## Sample output

```text
3
```

## Solution

```python
import functools


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@count_calls
def greet(name):
    return f"hi {name}"


n = int(input())
for _ in range(n):
    greet(input().strip())
print(greet.calls)
```

## Explanation

- The decorator attaches state to the wrapper function itself, so every call updates the same counter.
- `functools.wraps` keeps the original name and docstring visible.
