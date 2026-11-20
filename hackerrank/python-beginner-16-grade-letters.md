# Letter Grades

- **Language:** Python
- **Level:** Beginner
- **Topic:** Functions and conditionals
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` and `n` scores. Print a letter for each score: `A` for 90 and above, `B` for 80 to 89, `C` for 70 to 79, otherwise `F`. Separate the letters with spaces.

## Input format

Line 1: `n`. Line 2: `n` scores.

## Output format

One line of letters.

## Sample input

```text
4
95 82 70 59
```

## Sample output

```text
A B C F
```

## Solution

```python
def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "F"


n = int(input())
print(" ".join(grade(int(s)) for s in input().split()))
```

## Explanation

- Checking from the highest threshold down means each `if` only needs a lower bound.
