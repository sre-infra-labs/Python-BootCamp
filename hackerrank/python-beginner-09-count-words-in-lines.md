# Count Words in Several Lines

- **Language:** Python
- **Level:** Beginner
- **Topic:** Input loops
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n`, then `n` lines of text. Print the total number of words across all lines.

## Input format

Line 1: `n`. Then `n` lines of text.

## Output format

One integer: the total word count.

## Sample input

```text
2
hello world
the quick brown fox
```

## Sample output

```text
6
```

## Solution

```python
n = int(input())
total = sum(len(input().split()) for _ in range(n))
print(total)
```

## Explanation

- `split()` with no argument splits on any run of whitespace.
