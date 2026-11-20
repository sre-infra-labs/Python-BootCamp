# Flatten a Nested List

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Recursion and generators
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read one line that holds a Python list which may contain other lists. Print all the values in order, flattened, separated by spaces.

## Input format

One line with a list literal, for example `[1, [2, [3, 4]], 5]`.

## Output format

One line of values.

## Sample input

```text
[1, [2, [3, 4]], 5]
```

## Sample output

```text
1 2 3 4 5
```

## Solution

```python
import ast


def flatten(items):
    for item in items:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


data = ast.literal_eval(input())
print(" ".join(map(str, flatten(data))))
```

## Explanation

- `ast.literal_eval` parses a literal safely, unlike `eval`.
- `yield from` passes the values of the inner call up to the caller.
