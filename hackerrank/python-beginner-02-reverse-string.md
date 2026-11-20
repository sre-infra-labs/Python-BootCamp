# Reverse a String

- **Language:** Python
- **Level:** Beginner
- **Topic:** Strings
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read one string and print it reversed.

## Input format

One line containing a string with no leading or trailing spaces.

## Output format

The reversed string.

## Sample input

```text
hackerrank
```

## Sample output

```text
knarrekcah
```

## Solution

```python
s = input()
print(s[::-1])
```

## Explanation

- `s[::-1]` is a slice with step -1, which walks the string backwards.
