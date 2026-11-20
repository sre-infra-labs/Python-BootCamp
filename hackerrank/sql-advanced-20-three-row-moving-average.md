# Three-Row Moving Average of Salary

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Window frames
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

In hire-date order, show each employee with the average salary of that row and the two rows before it, rounded to two decimals. Use the rows, not a date range.

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

One line per employee: `name | moving_avg`.

## Solution

```sql
SELECT name,
       ROUND(AVG(salary) OVER (ORDER BY hire_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS moving_avg
FROM employees
ORDER BY hire_date;
```

## Expected output

```text
Carol | 52000.0
Alice | 68500.0
Asha | 65666.67
Bob | 71666.67
Dan | 59333.33
Ravi | 62666.67
```

## Explanation

- The first rows have fewer than three values, so the average uses what is available.
