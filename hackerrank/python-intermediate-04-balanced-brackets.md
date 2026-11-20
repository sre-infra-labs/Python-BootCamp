# Balanced Brackets

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Stacks
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read a line that contains only the characters `(`, `)`, `[`, `]`, `{`, `}`. Print `YES` if every bracket is closed in the correct order, otherwise `NO`.

## Input format

One line of brackets.

## Output format

`YES` or `NO`.

## Sample input

```text
{[()]}
```

## Sample output

```text
YES
```

## Solution

```python
s = input().strip()
pairs = {")": "(", "]": "[", "}": "{"}
stack = []
ok = True
for ch in s:
    if ch in "([{":
        stack.append(ch)
    elif not stack or stack.pop() != pairs[ch]:
        ok = False
        break
print("YES" if ok and not stack else "NO")
```

## Explanation

- A stack holds the open brackets. Each closing bracket must match the most recent one.
- Any unmatched opener left on the stack at the end means `NO`.
