# Connected Components with Union-Find

- **Language:** Python
- **Level:** Advanced
- **Topic:** Disjoint set union
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` nodes (numbered 1 to n) and `m` undirected edges. Print the number of connected components.

## Input format

Line 1: `n m`. Then `m` lines `u v`.

## Output format

One integer.

## Sample input

```text
5 3
1 2
2 3
4 5
```

## Sample output

```text
2
```

## Solution

```python
n, m = map(int, input().split())
parent = list(range(n + 1))


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # path halving
        x = parent[x]
    return x


components = n
for _ in range(m):
    u, v = map(int, input().split())
    ru, rv = find(u), find(v)
    if ru != rv:
        parent[ru] = rv
        components -= 1
print(components)
```

## Explanation

- Each successful union reduces the component count by one.
