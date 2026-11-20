# Longest Common Prefix

- **Language:** Python
- **Level:** Intermediate
- **Topic:** String comparison
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` words. Print the longest prefix shared by all of them. Print an empty line if there is none.

## Input format

Line 1: `n`. Then `n` words.

## Output format

The prefix.

## Sample input

```text
3
flower
flow
flight
```

## Sample output

```text
fl
```

## Solution

```python
n = int(input())
words = [input().strip() for _ in range(n)]
prefix = words[0]
for w in words[1:]:
    while not w.startswith(prefix):
        prefix = prefix[:-1]
print(prefix)
```

## Explanation

- Shorten the prefix until each word starts with it. An empty prefix matches everything, so the loop always ends.
