# Rank Employees Within Each Department

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Window functions
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Rank the employees inside each department by salary, highest first. Equal salaries share a rank. Show department, name, salary and rank. Sort by department, then rank, then name.

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

One line per employee: `name | dept | salary | rank`.

## Solution

```sql
SELECT name, dept, salary,
       RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk
FROM employees
ORDER BY dept, rnk, name;
```

## Expected output

```text
Alice | Engineering | 85000 | 1
Bob | Engineering | 70000 | 2
Ravi | Engineering | 70000 | 2
Asha | Marketing | 60000 | 1
Carol | Sales | 52000 | 1
Dan | Sales | 48000 | 2
```

## Explanation

- `PARTITION BY dept` restarts the ranking for each department.
- `RANK` gives tied rows the same rank and skips the next number. `DENSE_RANK` would not skip it.
