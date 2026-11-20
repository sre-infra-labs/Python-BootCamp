# Employees in Chennai Offices

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** JOIN
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List the name and office location of each employee whose department is in Chennai. Sort by name.

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

One line per employee: `name | location`.

## Solution

```sql
SELECT e.name, d.location
FROM employees e
JOIN departments d ON e.dept = d.name
WHERE d.location = 'Chennai'
ORDER BY e.name;
```

## Expected output

```text
Asha | Chennai
Carol | Chennai
Dan | Chennai
```

## Explanation

- An inner `JOIN` keeps only employees whose department exists in `departments`.
- The filter on `location` runs after the join, so it can use the department's column.
