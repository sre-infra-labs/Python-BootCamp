# Pascal's Triangle

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Lists and iteration
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` and print the first `n` rows of Pascal's triangle. Each row is printed with its numbers separated by spaces.

## Input format

One integer `n`.

## Output format

`n` lines.

## Sample input

```text
4
```

## Sample output

```text
1
1 1
1 2 1
1 3 3 1
```

## Solution

```python
n = int(input())
row = [1]
for _ in range(n):
    print(" ".join(map(str, row)))
    row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
```

## Explanation

- Each new row adds neighbours of the previous row, with a 1 at each end.
