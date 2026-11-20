# Group Anagrams

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Grouping with dict
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` words. Group the words that are anagrams of each other. Print each group on one line, in the order the groups first appear, with words in their original order.

## Input format

Line 1: `n`. Then `n` words.

## Output format

One line per group.

## Sample input

```text
4
eat
tea
tan
ate
```

## Sample output

```text
eat tea ate
tan
```

## Solution

```python
from collections import defaultdict

n = int(input())
groups = defaultdict(list)
for _ in range(n):
    word = input().strip()
    groups["".join(sorted(word))].append(word)
for words in groups.values():
    print(" ".join(words))
```

## Explanation

- The sorted letters of a word are the same for all of its anagrams, so they work as a dictionary key.
