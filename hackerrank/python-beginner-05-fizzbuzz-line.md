# FizzBuzz on One Line

- **Language:** Python
- **Level:** Beginner
- **Topic:** Conditionals
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n`. Print the numbers 1 to n on one line, separated by spaces. Replace multiples of 3 with `Fizz`, multiples of 5 with `Buzz`, and multiples of both with `FizzBuzz`.

## Input format

One integer `n`.

## Output format

One line of `n` values separated by spaces.

## Sample input

```text
5
```

## Sample output

```text
1 2 Fizz 4 Buzz
```

## Solution

```python
n = int(input())
out = []
for i in range(1, n + 1):
    if i % 15 == 0:
        out.append("FizzBuzz")
    elif i % 3 == 0:
        out.append("Fizz")
    elif i % 5 == 0:
        out.append("Buzz")
    else:
        out.append(str(i))
print(" ".join(out))
```

## Explanation

- Check the multiple of 15 first. Otherwise a multiple of 15 would print only `Fizz`.
