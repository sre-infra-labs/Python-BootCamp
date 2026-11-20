# Stacked Tag Decorators

- **Language:** Python
- **Level:** Intermediate
- **Topic:** Stacking decorators
- **Practice more:** https://www.hackerrank.com/domains/python

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Define a `tag(name)` decorator factory that wraps the returned string in `<name>` and `</name>`. Apply `@tag("b")` on top of `@tag("i")` to a function that returns its input. Read a word and print the result.

## Input format

One word.

## Output format

The word wrapped in `<b><i>` and `</i></b>`.

## Sample input

```text
hi
```

## Sample output

```text
<b><i>hi</i></b>
```

## Solution

```python
def tag(name):
    def decorator(func):
        def wrapper(text):
            return f"<{name}>{func(text)}</{name}>"
        return wrapper
    return decorator


@tag("b")
@tag("i")
def emphasise(text):
    return text


print(emphasise(input().strip()))
```

## Explanation

- Decorators apply bottom-up: `@tag("i")` wraps the function first, then `@tag("b")` wraps that result.
