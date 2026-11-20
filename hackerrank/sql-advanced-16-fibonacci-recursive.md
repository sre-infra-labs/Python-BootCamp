# First Ten Fibonacci Numbers

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Recursive CTE
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Generate the first ten Fibonacci numbers with a recursive CTE. Show the position and the value, where position 1 has value 0.

## Dataset

Create and load these tables first:

```sql
CREATE TABLE departments (name TEXT PRIMARY KEY, location TEXT);
INSERT INTO departments VALUES ('Engineering','Bangalore'),('Sales','Chennai'),('Marketing','Chennai');
CREATE TABLE employees (id INTEGER PRIMARY KEY, name TEXT, dept TEXT, salary INTEGER, hire_date TEXT, manager_id INTEGER);
INSERT INTO employees VALUES
(1,'Alice','Engineering',85000,'2019-03-01',NULL),
(2,'Bob','Engineering',70000,'2020-06-15',1),
(3,'Carol','Sales',52000,'2018-11-20',NULL),
(4,'Dan','Sales',48000,'2021-01-10',3),
(5,'Asha','Marketing',60000,'2020-02-05',NULL),
(6,'Ravi','Engineering',70000,'2021-07-07',1);
```

## Output format

One line per position: `n | value`.

## Solution

```sql
WITH RECURSIVE fib(n, a, b) AS (
    SELECT 1, 0, 1
    UNION ALL
    SELECT n + 1, b, a + b FROM fib WHERE n < 10
)
SELECT n, a FROM fib ORDER BY n;
```

## Expected output

```text
1 | 0
2 | 1
3 | 1
4 | 2
5 | 3
6 | 5
7 | 8
8 | 13
9 | 21
10 | 34
```

## Explanation

- Each row carries the current and next Fibonacci numbers, so the next row is `(b, a + b)`.
