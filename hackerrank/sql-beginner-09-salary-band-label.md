# Label Salaries by Band

- **Language:** SQL
- **Level:** Beginner
- **Topic:** CASE
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each employee, show a band: `High` for 70000 and above, `Medium` for 55000 to 69999, and `Standard` otherwise. Sort by name.

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

One line per employee: `name | band`.

## Solution

```sql
SELECT name,
       CASE WHEN salary >= 70000 THEN 'High'
            WHEN salary >= 55000 THEN 'Medium'
            ELSE 'Standard'
       END AS band
FROM employees
ORDER BY name;
```

## Expected output

```text
Alice | High
Asha | Medium
Bob | High
Carol | Standard
Dan | Standard
Ravi | High
```

## Explanation

- `CASE` checks conditions in order and stops at the first one that is true.
