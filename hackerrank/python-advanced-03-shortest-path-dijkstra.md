# Shortest Path in a Weighted Graph

- **Language:** Python
- **Level:** Advanced
- **Topic:** Graphs and heaps
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

The graph is undirected and has positive edge weights. Read `n` nodes numbered 1 to `n`, then `m` edges as `u v w`. Then read the start node `s` and target node `t`. Print the shortest distance from `s` to `t`, or `-1` if `t` is unreachable.

## Input format

Line 1: `n m`. Next `m` lines: `u v w`. Last line: `s t`.

## Output format

One integer: the shortest distance, or -1.

## Sample input

```text
4 4
1 2 4
1 3 1
3 2 2
2 4 5
1 4
```

## Sample output

```text
8
```

## Solution

```python
import heapq

n, m = map(int, input().split())
adj = {node: [] for node in range(1, n + 1)}
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

s, t = map(int, input().split())
dist = {s: 0}
heap = [(0, s)]
while heap:
    d, u = heapq.heappop(heap)
    if d > dist.get(u, float("inf")):
        continue  # stale entry
    for v, w in adj[u]:
        nd = d + w
        if nd < dist.get(v, float("inf")):
            dist[v] = nd
            heapq.heappush(heap, (nd, v))

print(dist.get(t, -1))
```

## Explanation

- Dijkstra's algorithm: a min-heap always expands the closest unvisited node.
- A popped entry larger than the best known distance is stale, so it is skipped.
- The sample answer is 8 (1 to 3 to 2 to 4), not 9 (1 to 2 to 4), because 1 to 3 to 2 is cheaper.
