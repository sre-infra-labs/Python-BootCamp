# Leap Year Check

- **Language:** Python
- **Level:** Beginner
- **Topic:** Conditionals
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line of years. For each year print `Leap` or `Not Leap`. A year is a leap year if it is divisible by 4, except century years, which must be divisible by 400.

## Input format

One line of integers.

## Output format

One line per year.

## Sample input

```text
1900 2000 2024 2023
```

## Sample output

```text
Not Leap
Leap
Leap
Not Leap
```

## Solution

```python
for year in map(int, input().split()):
    leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    print("Leap" if leap else "Not Leap")
```

## Explanation

- 1900 is not a leap year because it is a century year not divisible by 400.
