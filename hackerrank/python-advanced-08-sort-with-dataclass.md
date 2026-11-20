# Sort People with a Dataclass

- **Language:** Python
- **Level:** Advanced
- **Topic:** Dataclasses
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Read `n`, then `n` lines `name age`. Store each person in a dataclass that orders by age, then by name. Print the sorted people as `name age`.

## Input format

Line 1: `n`. Then `n` lines `name age`.

## Output format

`n` lines `name age` in sorted order.

## Sample input

```text
3
zoe 30
an 25
bo 30
```

## Sample output

```text
an 25
bo 30
zoe 30
```

## Solution

```python
from dataclasses import dataclass


@dataclass(order=True)
class Person:
    age: int
    name: str


n = int(input())
people = []
for _ in range(n):
    name, age = input().split()
    people.append(Person(int(age), name))
for p in sorted(people):
    print(p.name, p.age)
```

## Explanation

- With `order=True`, the dataclass compares fields in declaration order: age first, then name.
- Putting `age` first in the class is what makes the sort use age as the primary key.
