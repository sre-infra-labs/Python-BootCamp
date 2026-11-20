# Collatz Sequence from 6

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Recursive CTE
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Starting from 6, apply the Collatz rule until you reach 1: if the number is even, halve it; if it is odd, multiply by 3 and add 1. Show each step number and value.

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

One line per step: `step | value`.

## Solution

```sql
WITH RECURSIVE collatz(step, n) AS (
    SELECT 0, 6
    UNION ALL
    SELECT step + 1,
           CASE WHEN n = 1 THEN 1 WHEN n % 2 = 0 THEN n / 2 ELSE 3 * n + 1 END
    FROM collatz
    WHERE n <> 1
)
SELECT step, n FROM collatz ORDER BY step;
```

## Expected output

```text
0 | 6
1 | 3
2 | 10
3 | 5
4 | 16
5 | 8
6 | 4
7 | 2
8 | 1
```

## Explanation

- The recursion stops as soon as `n` reaches 1.
