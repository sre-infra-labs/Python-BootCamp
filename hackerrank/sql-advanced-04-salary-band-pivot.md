# Salary Bands per Department

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Conditional aggregation
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each department, count the employees in three bands: low (below 55000), mid (55000 to 69999), and high (70000 and above). Show one row per department. Sort by department.

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

One line per department: `dept | low | mid | high`.

## Solution

```sql
SELECT dept,
       SUM(CASE WHEN salary < 55000 THEN 1 ELSE 0 END) AS low,
       SUM(CASE WHEN salary >= 55000 AND salary < 70000 THEN 1 ELSE 0 END) AS mid,
       SUM(CASE WHEN salary >= 70000 THEN 1 ELSE 0 END) AS high
FROM employees
GROUP BY dept
ORDER BY dept;
```

## Expected output

```text
Engineering | 0 | 0 | 3
Marketing | 0 | 1 | 0
Sales | 2 | 0 | 0
```

## Explanation

- Each `CASE` turns one band into a 1 or 0, and `SUM` counts them per department.
- This is a manual pivot. Use `FILTER (WHERE ...)` on PostgreSQL for a shorter form.
