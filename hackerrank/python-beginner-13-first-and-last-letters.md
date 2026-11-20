# First and Last Letter of Each Word

- **Language:** Python
- **Level:** Beginner
- **Topic:** Strings and split
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line of words. For each word print its first letter followed by its last letter. Join the results with spaces.

## Input format

One line of words.

## Output format

One line.

## Sample input

```text
hello world
```

## Sample output

```text
ho wd
```

## Solution

```python
print(" ".join(w[0] + w[-1] for w in input().split()))
```

## Explanation

- `w[-1]` is the last character, and negative indexes count from the end.
