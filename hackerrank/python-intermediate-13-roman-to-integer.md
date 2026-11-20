# Roman Numeral to Integer

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Parsing rules
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a Roman numeral and print its integer value. A smaller symbol before a larger one is subtracted, as in `IV` = 4.

## Input format

One Roman numeral.

## Output format

One integer.

## Sample input

```text
MCMXCIV
```

## Sample output

```text
1994
```

## Solution

```python
values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
s = input().strip()
total = 0
for i, ch in enumerate(s):
    v = values[ch]
    if i + 1 < len(s) and v < values[s[i + 1]]:
        total -= v
    else:
        total += v
print(total)
```

## Explanation

- Each symbol is subtracted when the next symbol is larger, and added otherwise.
