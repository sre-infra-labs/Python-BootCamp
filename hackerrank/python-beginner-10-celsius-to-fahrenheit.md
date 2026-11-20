# Celsius to Fahrenheit

- **Language:** Python
- **Level:** Beginner
- **Topic:** Floats and formatting
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n`, then one line with `n` temperatures in Celsius. Print each temperature in Fahrenheit, rounded to one decimal place, separated by spaces. Use F = C × 9/5 + 32.

## Input format

Line 1: `n`. Line 2: `n` numbers.

## Output format

One line of Fahrenheit values.

## Sample input

```text
3
0 100 -40
```

## Sample output

```text
32.0 212.0 -40.0
```

## Solution

```python
input()
temps = map(float, input().split())
print(" ".join(f"{c * 9 / 5 + 32:.1f}" for c in temps))
```

## Explanation

- `:.1f` formats a float with one decimal place.
- `-40` is the same in both scales, which makes a good check.
