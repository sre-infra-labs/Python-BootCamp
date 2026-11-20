# Average Salary per Department from CSV Lines

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Parsing and grouping
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n`, then `n` lines in the form `name,dept,salary`. Print the average salary of each department with two decimals, departments sorted by name.

## Input format

Line 1: `n`. Then `n` lines `name,dept,salary`.

## Output format

One line per department: `dept: average`.

## Sample input

```text
4
alice,Eng,100
bob,Eng,200
carol,Ops,150
dan,Ops,100
```

## Sample output

```text
Eng: 150.00
Ops: 125.00
```

## Solution

```python
from collections import defaultdict

n = int(input())
totals = defaultdict(lambda: [0, 0])  # dept -> [sum, count]
for _ in range(n):
    name, dept, salary = input().split(",")
    totals[dept][0] += int(salary)
    totals[dept][1] += 1
for dept in sorted(totals):
    total, count = totals[dept]
    print(f"{dept}: {total / count:.2f}")
```

## Explanation

- Each department keeps a running sum and a count, so the average needs one pass.
- Sorting the keys gives the output in name order.
