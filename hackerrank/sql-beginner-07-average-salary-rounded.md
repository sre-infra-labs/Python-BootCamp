# Average Salary Rounded to Two Decimals

- **Language:** SQL
- **Level:** Beginner
- **Topic:** ROUND
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Find the average salary of all employees, rounded to two decimal places.

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

One value.

## Solution

```sql
SELECT ROUND(AVG(salary), 2) AS avg_salary FROM employees;
```

## Expected output

```text
64166.67
```

## Explanation

- `AVG` ignores NULLs. `ROUND(x, 2)` keeps two decimals.
