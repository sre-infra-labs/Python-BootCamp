# Palindrome Check

- **Language:** Python
- **Level:** Beginner
- **Topic:** Strings
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a word and print `YES` if it reads the same forwards and backwards, ignoring case. Otherwise print `NO`.

## Input format

One line containing a word.

## Output format

`YES` or `NO`.

## Sample input

```text
Racecar
```

## Sample output

```text
YES
```

## Solution

```python
s = input().strip().lower()
print("YES" if s == s[::-1] else "NO")
```

## Explanation

- Lower-casing first makes `Racecar` match.
- `s[::-1]` is the reversed string, so equality means palindrome.
