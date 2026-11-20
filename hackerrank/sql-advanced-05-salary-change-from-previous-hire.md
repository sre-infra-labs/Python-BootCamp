# Salary Change from the Previous Hire

- **Language:** SQL
- **Level:** Advanced
- **Topic:** LAG
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

In hire-date order, show each name, salary, and the difference from the previous hire's salary. The first hire has no previous row, so show NULL.

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

One line per employee: `name | salary | diff`. NULL is printed as `NULL`.

## Solution

```sql
SELECT name, salary,
       salary - LAG(salary) OVER (ORDER BY hire_date) AS diff_from_prev
FROM employees
ORDER BY hire_date;
```

## Expected output

```text
Carol | 52000 | NULL
Alice | 85000 | 33000
Asha | 60000 | -25000
Bob | 70000 | 10000
Dan | 48000 | -22000
Ravi | 70000 | 22000
```

## Explanation

- `LAG(salary)` reads the value from the previous row in the window order.
- The first row has no previous row, so the result is NULL.
