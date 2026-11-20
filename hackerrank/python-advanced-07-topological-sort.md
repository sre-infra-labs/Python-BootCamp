# Topological Order

- **Language:** Python
- **Level:** Advanced
- **Topic:** Graphs
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

The graph is a directed acyclic graph with nodes 1 to `n`. Each edge `u v` means `u` must come before `v`. Print one valid order. When several nodes are available, take the smallest number first.

## Input format

Line 1: `n m`. Next `m` lines: `u v`.

## Output format

One line with the order.

## Sample input

```text
4 3
4 2
3 2
1 4
```

## Sample output

```text
1 3 4 2
```

## Solution

```python
import heapq

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
indegree = {i: 0 for i in range(1, n + 1)}
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1

ready = [node for node in indegree if indegree[node] == 0]
heapq.heapify(ready)
order = []
while ready:
    u = heapq.heappop(ready)
    order.append(u)
    for v in graph[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(ready, v)
print(" ".join(map(str, order)))
```

## Explanation

- Kahn's algorithm: start with nodes that have no incoming edges.
- A min-heap for the ready nodes gives the smallest-first order.
