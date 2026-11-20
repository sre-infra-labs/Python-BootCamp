# Anagram Check

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Strings and sorting
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read two lines. Print `Anagram` if they use the same letters with the same counts, ignoring case and spaces. Otherwise print `Not Anagram`.

## Input format

Two lines, each a phrase of letters and spaces.

## Output format

`Anagram` or `Not Anagram`.

## Sample input

```text
Listen
Silent
```

## Sample output

```text
Anagram
```

## Solution

```python
a = input().replace(" ", "").lower()
b = input().replace(" ", "").lower()
print("Anagram" if sorted(a) == sorted(b) else "Not Anagram")
```

## Explanation

- Two strings are anagrams when their sorted characters match.
- Normalise case and spaces first, so `Listen` and `Silent` compare equal.
