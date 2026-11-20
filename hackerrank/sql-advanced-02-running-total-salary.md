# Running Total of Salary by Hire Date

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Window frames
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For employees in hire-date order, show each name, hire date, salary, and the total salary paid so far, including the current row.

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

One line per employee: `name | hire_date | salary | running_total`.

## Solution

```sql
SELECT name, hire_date, salary,
       SUM(salary) OVER (ORDER BY hire_date
                         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM employees
ORDER BY hire_date;
```

## Expected output

```text
Carol | 2018-11-20 | 52000 | 52000
Alice | 2019-03-01 | 85000 | 137000
Asha | 2020-02-05 | 60000 | 197000
Bob | 2020-06-15 | 70000 | 267000
Dan | 2021-01-10 | 48000 | 315000
Ravi | 2021-07-07 | 70000 | 385000
```

## Explanation

- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` makes the sum accumulate from the first row to the current one.
