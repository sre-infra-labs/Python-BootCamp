# Employees Hired in 2020 or Later

- **Language:** SQL
- **Level:** Beginner
- **Topic:** Date comparison
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List the names of employees hired on or after 2020-01-01. Sort by name.

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

One name per line.

## Solution

```sql
SELECT name FROM employees WHERE hire_date >= '2020-01-01' ORDER BY name;
```

## Expected output

```text
Asha
Bob
Dan
Ravi
```

## Explanation

- ISO dates (`YYYY-MM-DD`) compare correctly as text.
