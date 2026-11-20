# First N Primes with a Generator

- **Language:** Python
- **Level:** Advanced
- **Topic:** Generators
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Write a generator `primes()` that yields prime numbers in order without end. Read `n` and print the first `n` primes, separated by spaces.

## Input format

One integer `n`.

## Output format

One line with `n` primes.

## Sample input

```text
6
```

## Sample output

```text
2 3 5 7 11 13
```

## Solution

```python
from itertools import islice


def primes():
    found = []
    candidate = 2
    while True:
        if all(candidate % p for p in found if p * p <= candidate):
            found.append(candidate)
            yield candidate
        candidate += 1


n = int(input())
print(" ".join(map(str, islice(primes(), n))))
```

## Explanation

- A generator produces values lazily, so the function never needs to know `n`.
- A candidate is prime if no earlier prime up to its square root divides it.
- `islice` takes only the first `n` values from the infinite generator.
