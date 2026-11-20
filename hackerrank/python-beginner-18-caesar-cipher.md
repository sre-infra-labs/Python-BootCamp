# Caesar Cipher

- **Language:** Python
- **Level:** Beginner
- **Topic:** chr and ord
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a shift `k` and a line of text. Shift each lowercase letter forward by `k` places, wrapping from `z` back to `a`. Leave all other characters unchanged.

## Input format

Line 1: `k`. Line 2: the text.

## Output format

The encoded text.

## Sample input

```text
3
xyz abc
```

## Sample output

```text
abc def
```

## Solution

```python
k = int(input())
text = input().strip()
out = []
for ch in text:
    if "a" <= ch <= "z":
        out.append(chr((ord(ch) - ord("a") + k) % 26 + ord("a")))
    else:
        out.append(ch)
print("".join(out))
```

## Explanation

- Subtracting `ord('a')` maps letters to 0-25, so the modulo handles the wrap.
