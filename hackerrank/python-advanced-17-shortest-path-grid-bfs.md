# Shortest Path in a Grid

- **Language:** Python
- **Level:** Advanced
- **Topic:** BFS on a grid
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a grid with `S` (start), `E` (end), `#` (wall) and `.` (open). You can move up, down, left or right. Print the fewest moves from `S` to `E`, or -1 if `E` cannot be reached.

## Input format

Line 1: `r c`. Then `r` lines of `c` characters.

## Output format

One integer.

## Sample input

```text
3 4
S..#
.#..
...E
```

## Sample output

```text
5
```

## Solution

```python
from collections import deque

r, c = map(int, input().split())
grid = [input() for _ in range(r)]
start = end = None
for i in range(r):
    for j in range(c):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)

dist = {start: 0}
queue = deque([start])
while queue:
    i, j = queue.popleft()
    if (i, j) == end:
        break
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] != "#" and (ni, nj) not in dist:
            dist[(ni, nj)] = dist[(i, j)] + 1
            queue.append((ni, nj))
print(dist.get(end, -1))
```

## Explanation

- BFS explores cells in order of distance, so the first time `E` is reached is the shortest path.
