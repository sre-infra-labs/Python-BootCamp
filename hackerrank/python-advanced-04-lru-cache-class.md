# LRU Cache

- **Language:** Python
- **Level:** Advanced
- **Topic:** Data structures
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Implement a least-recently-used cache with capacity `c`. Read `c`, then `q` operations. `put k v` stores a value and evicts the least recently used key when the cache is full. `get k` prints the value, or `-1` if the key is absent. Both `put` and a successful `get` mark the key as most recently used.

## Input format

Line 1: `c`. Line 2: `q`. Then `q` lines: `put k v` or `get k`.

## Output format

One line for each `get`: the value or -1.

## Sample input

```text
2
6
put a 1
put b 2
get a
put c 3
get b
get c
```

## Sample output

```text
1
-1
3
```

## Solution

```python
from collections import OrderedDict

capacity = int(input())
q = int(input())
cache = OrderedDict()

for _ in range(q):
    parts = input().split()
    if parts[0] == "put":
        key, value = parts[1], parts[2]
        if key in cache:
            cache.move_to_end(key)
        cache[key] = value
        if len(cache) > capacity:
            cache.popitem(last=False)  # evict least recently used
    else:
        key = parts[1]
        if key in cache:
            cache.move_to_end(key)
            print(cache[key])
        else:
            print(-1)
```

## Explanation

- `OrderedDict` keeps keys in usage order. `move_to_end` marks a key as recently used.
- `popitem(last=False)` removes the oldest entry, which is the least recently used one.
