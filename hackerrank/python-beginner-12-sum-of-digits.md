# Sum of Digits

- **Language:** Python
- **Level:** Beginner
- **Topic:** Integers
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a non-negative integer and print the sum of its digits.

## Input format

One integer.

## Output format

One integer.

## Sample input

```text
98765
```

## Sample output

```text
35
```

## Solution

```python
n = input().strip()
print(sum(int(d) for d in n))
```

## Explanation

- Working on the string of digits avoids repeated division and modulo.
