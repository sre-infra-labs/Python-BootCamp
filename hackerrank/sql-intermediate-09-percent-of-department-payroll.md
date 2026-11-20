# Share of Department Payroll

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Window SUM
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each employee, show the percentage of their department's total salary that they earn. Round to one decimal. Sort by department, then name.

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

One line per employee: `name | dept | percent`.

## Solution

```sql
SELECT name, dept,
       ROUND(100.0 * salary / SUM(salary) OVER (PARTITION BY dept), 1) AS pct
FROM employees
ORDER BY dept, name;
```

## Expected output

```text
Alice | Engineering | 37.8
Bob | Engineering | 31.1
Ravi | Engineering | 31.1
Asha | Marketing | 100.0
Carol | Sales | 52.0
Dan | Sales | 48.0
```

## Explanation

- A window `SUM` with `PARTITION BY` gives each department total on every row, without collapsing the rows.
- `100.0 *` forces decimal division.
