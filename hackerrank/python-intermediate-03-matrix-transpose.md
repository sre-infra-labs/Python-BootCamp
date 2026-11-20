# Matrix Transpose

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Lists of lists
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read an `r` by `c` matrix of integers and print its transpose. The transpose has `c` rows and `r` columns.

## Input format

First line: `r c`. Then `r` lines with `c` integers each.

## Output format

`c` lines with `r` integers each.

## Sample input

```text
2 3
1 2 3
4 5 6
```

## Sample output

```text
1 4
2 5
3 6
```

## Solution

```python
r, c = map(int, input().split())
matrix = [input().split() for _ in range(r)]
for j in range(c):
    print(" ".join(matrix[i][j] for i in range(r)))
```

## Explanation

- Row `j` of the result is column `j` of the input.
- Values are kept as strings here, since only printing is needed.
