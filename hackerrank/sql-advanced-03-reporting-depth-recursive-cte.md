# Depth in the Reporting Tree

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Recursive CTE
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Each employee may have a manager (`manager_id`). Employees with no manager are at depth 0. Everyone else is one level below their manager. Show each name and depth, sorted by depth, then name.

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

One line per employee: `name | depth`.

## Solution

```sql
WITH RECURSIVE chain(id, name, depth) AS (
    SELECT id, name, 0 FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, c.depth + 1
    FROM employees e
    JOIN chain c ON e.manager_id = c.id
)
SELECT name, depth FROM chain ORDER BY depth, name;
```

## Expected output

```text
Alice | 0
Asha | 0
Carol | 0
Bob | 1
Dan | 1
Ravi | 1
```

## Explanation

- The anchor query selects the top of each tree. The recursive part adds the employees who report to the rows already found.
- Recursion stops when no new rows join. Use `UNION ALL` only when cycles are impossible.
