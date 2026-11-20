# Employees by Department and Salary

- **Language:** SQL
- **Level:** Beginner
- **Topic:** Multi-column ORDER BY
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List every employee with department and salary. Sort by department, then by salary from highest to lowest, then by name.

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

One line per employee: `name | dept | salary`.

## Solution

```sql
SELECT name, dept, salary FROM employees ORDER BY dept, salary DESC, name;
```

## Expected output

```text
Alice | Engineering | 85000
Bob | Engineering | 70000
Ravi | Engineering | 70000
Asha | Marketing | 60000
Carol | Sales | 52000
Dan | Sales | 48000
```

## Explanation

- Each column in `ORDER BY` is used only to break ties in the one before it.
