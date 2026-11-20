# Top Three Earners

- **Language:** SQL
- **Level:** Beginner
- **Topic:** ORDER BY and LIMIT
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List the three highest salaries with the employee name. Break ties by name.

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

One line per employee: `name | salary`.

## Solution

```sql
SELECT name, salary FROM employees ORDER BY salary DESC, name ASC LIMIT 3;
```

## Expected output

```text
Alice | 85000
Bob | 70000
Ravi | 70000
```

## Explanation

- `LIMIT` is applied after `ORDER BY`.
- The second `ORDER BY` column breaks ties predictably.
