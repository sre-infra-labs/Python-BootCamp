# Word Frequency in First-Seen Order

- **Language:** Python
- **Level:** Beginner
- **Topic:** Dictionaries
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line of words. For each distinct word, print the word and how many times it appears. Print the words in the order they first appear.

## Input format

One line of space-separated words.

## Output format

One line per distinct word: the word, a space, and its count.

## Sample input

```text
the cat the dog
```

## Sample output

```text
the 2
cat 1
dog 1
```

## Solution

```python
from collections import Counter

words = input().split()
counts = Counter(words)
for word in dict.fromkeys(words):  # keeps first-seen order
    print(word, counts[word])
```

## Explanation

- `Counter` counts occurrences.
- `dict.fromkeys(words)` gives the distinct words in first-seen order, because dictionaries keep insertion order.
