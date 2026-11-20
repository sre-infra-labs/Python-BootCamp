# Prefix Decorator Factory

- **Language:** Python
- **Level:** Advanced
- **Topic:** Decorator factories
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a decorator factory `prefix(label)` that prepends `[label] ` to the returned text. Apply `@prefix("INFO")` to `describe`, which strips and capitalises its input. Read a line and print the result.

## Input format

One line of text, possibly with extra spaces.

## Output format

The prefixed text.

## Sample input

```text
  server started
```

## Sample output

```text
[INFO] Server started
```

## Solution

```python
import functools


def prefix(label):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(msg):
            return f"[{label}] {func(msg)}"
        return wrapper
    return decorator


@prefix("INFO")
def describe(msg):
    return msg.strip().capitalize()


print(describe(input()))
```

## Explanation

- The label is captured by the factory, so each use of `@prefix` can have its own label.
