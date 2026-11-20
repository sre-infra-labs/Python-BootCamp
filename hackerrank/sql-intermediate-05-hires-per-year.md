# Hires per Year

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Date functions
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Count how many employees were hired in each calendar year. Sort by year.

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

One line per year: `year | hires`.

## Solution

```sql
SELECT substr(hire_date, 1, 4) AS year, COUNT(*) AS hires
FROM employees
GROUP BY substr(hire_date, 1, 4)
ORDER BY year;
```

## Expected output

```text
2018 | 1
2019 | 1
2020 | 2
2021 | 2
```

## Explanation

- Dates are stored as `YYYY-MM-DD` text here, so `substr` takes the year.
- On PostgreSQL you would use `EXTRACT(YEAR FROM hire_date)` with a real date type.
