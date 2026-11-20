# Deep Merge of Two Config Dicts

- **Language:** Python
- **Level:** Advanced
- **Topic:** Recursion over dicts
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read two Python dict literals on separate lines. Merge them deeply: nested dicts are merged key by key, and otherwise the value from the second dict wins. Print the result.

## Input format

Two lines, each a dict literal.

## Output format

The merged dict.

## Sample input

```text
{'db': {'host': 'localhost', 'port': 5432}, 'debug': False}
{'db': {'port': 5433}, 'debug': True}
```

## Sample output

```text
{'db': {'host': 'localhost', 'port': 5433}, 'debug': True}
```

## Solution

```python
import ast


def deep_merge(base, override):
    result = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


a = ast.literal_eval(input())
b = ast.literal_eval(input())
print(deep_merge(a, b))
```

## Explanation

- Nested dicts recurse, so only the changed leaves are overwritten.
- `ast.literal_eval` reads the literals without running any code.
