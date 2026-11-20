# Median Salary

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Window functions
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Find the median salary of all employees. If there is an even number of employees, use the average of the two middle values.

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
WITH ordered AS (
    SELECT salary,
           ROW_NUMBER() OVER (ORDER BY salary) AS rn,
           COUNT(*) OVER () AS cnt
    FROM employees
)
SELECT AVG(salary) AS median_salary
FROM ordered
WHERE rn IN ((cnt + 1) / 2, (cnt + 2) / 2);
```

## Expected output

```text
65000.0
```

## Explanation

- For `cnt` rows, the middle positions are `(cnt+1)/2` and `(cnt+2)/2` with integer division. They are the same position when `cnt` is odd.
- Averaging the two middle values gives the median for even counts.
