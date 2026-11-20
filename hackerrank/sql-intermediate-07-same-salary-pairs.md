# Pairs with the Same Salary

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Non-equi conditions
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List every pair of different employees who earn the same salary. Each pair should appear once. Sort by the first name.

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

One line per pair: `name1 | name2`.

## Solution

```sql
SELECT a.name, b.name
FROM employees a
JOIN employees b ON a.salary = b.salary AND a.id < b.id
ORDER BY a.name;
```

## Expected output

```text
Bob | Ravi
```

## Explanation

- `a.id < b.id` keeps each pair once and stops an employee from pairing with themselves.
