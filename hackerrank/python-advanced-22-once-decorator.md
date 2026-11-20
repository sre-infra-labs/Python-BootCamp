# Run Only Once

- **Language:** Python
- **Level:** Advanced
- **Topic:** Decorators with state
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a `once` decorator that runs the function on its first call only. Later calls do nothing and return `None`. Read `n`, then `n` names, call `setup(name)` for each, and let the function print `setup for <name>`.

## Input format

Line 1: `n`. Then `n` names.

## Output format

One line: the first setup message.

## Sample input

```text
3
a
b
c
```

## Sample output

```text
setup for a
```

## Solution

```python
import functools


def once(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
        return None
    wrapper.called = False
    return wrapper


@once
def setup(name):
    print(f"setup for {name}")


n = int(input())
for _ in range(n):
    setup(input().strip())
```

## Explanation

- The `called` flag is stored on the wrapper, so it persists between calls.
