# Count Words by Prefix

- **Language:** Python
- **Level:** Advanced
- **Topic:** Tries
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n` words and store them in a trie that keeps a count at each node. Then read `q` prefixes and print how many words start with each one.

## Input format

Line 1: `n`. Then `n` words. Then `q`, then `q` prefixes.

## Output format

One count per prefix.

## Sample input

```text
3
apple
app
apt
3
app
ap
b
```

## Sample output

```text
2
3
0
```

## Solution

```python
n = int(input())
root = {}
for _ in range(n):
    node = root
    for ch in input().strip():
        node = node.setdefault(ch, {"#count": 0})
        node["#count"] += 1

q = int(input())
for _ in range(q):
    node = root
    count = 0
    for ch in input().strip():
        if ch not in node:
            count = 0
            break
        node = node[ch]
        count = node["#count"]
    print(count)
```

## Explanation

- Each node stores how many words pass through it, so a prefix lookup is one walk down the trie.
