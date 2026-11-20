# Retry Decorator

- **Language:** Python
- **Level:** Advanced
- **Topic:** Retry logic
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write `retry(max_attempts)`. The decorated function is called again on `ValueError`, up to `max_attempts` times. If it succeeds, return the result and the attempt number. If all attempts fail, raise `RuntimeError`. Read `k`, the number of times `flaky` must fail before it succeeds. Print `ok after N attempts` or `failed after 3 attempts`.

## Input format

One integer `k`.

## Output format

One line.

## Sample input

```text
2
```

## Sample output

```text
ok after 3 attempts
```

## Solution

```python
import functools


def retry(max_attempts):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            last = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args), attempt
                except ValueError as exc:
                    last = exc
            raise RuntimeError(f"failed after {max_attempts} attempts") from last
        return wrapper
    return decorator


fail_times = int(input())
calls = {"n": 0}


@retry(max_attempts=3)
def flaky():
    calls["n"] += 1
    if calls["n"] <= fail_times:
        raise ValueError("temporary")
    return "ok"


try:
    result, attempts = flaky()
    print(f"{result} after {attempts} attempts")
except RuntimeError as exc:
    print(exc)
```

## Explanation

- `raise ... from last` keeps the last underlying error in the traceback.
- The decorator returns the attempt number, so the caller can report it.
