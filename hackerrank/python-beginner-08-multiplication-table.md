# Multiplication Table

- **Language:** Python
- **Level:** Beginner
- **Topic:** Loops and f-strings
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` and print its multiplication table from 1 to 10. Each line looks like `n x i = product`.

## Input format

One integer `n`.

## Output format

Ten lines, one per multiplier.

## Sample input

```text
3
```

## Sample output

```text
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

## Solution

```python
n = int(input())
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

## Explanation

- An f-string builds each line without manual string joining.
