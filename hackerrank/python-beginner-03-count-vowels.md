# Count the Vowels

- **Language:** Python
- **Level:** Beginner
- **Topic:** Strings
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line of text and print how many vowels (a, e, i, o, u) it contains. Count upper and lower case letters.

## Input format

One line of text.

## Output format

One integer: the number of vowels.

## Sample input

```text
Hello World
```

## Sample output

```text
3
```

## Solution

```python
s = input()
print(sum(1 for c in s.lower() if c in "aeiou"))
```

## Explanation

- `.lower()` makes the check case-insensitive.
- Membership test `c in "aeiou"` is simpler than a chain of `or` comparisons.
