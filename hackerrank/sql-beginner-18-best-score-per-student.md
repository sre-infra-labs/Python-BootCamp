# Best Score per Student

- **Language:** SQL
- **Level:** Beginner
- **Topic:** GROUP BY with join
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each student, show their highest score. Sort by name. Include students with no enrollments as NULL.

## Dataset

Create and load these tables first:

```sql
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, city TEXT);
INSERT INTO students VALUES (1,'Meena','Pune'),(2,'Kiran','Mumbai'),(3,'Leo','Pune'),(4,'Sara','Delhi'),(5,'Omar','Delhi');
CREATE TABLE courses (code TEXT PRIMARY KEY, title TEXT, credits INTEGER);
INSERT INTO courses VALUES ('CS101','Intro to Programming',4),('DB201','Databases',3),('ML301','Machine Learning',4),('AI401','Artificial Intelligence',3);
CREATE TABLE enrollments (student_id INTEGER, course_code TEXT, score INTEGER);
INSERT INTO enrollments VALUES (1,'CS101',88),(1,'DB201',92),(2,'CS101',75),(2,'ML301',81),(3,'DB201',67),(3,'CS101',90),(4,'CS101',55);
```

## Output format

One line per student: `name | best`.

## Solution

```sql
SELECT s.name, MAX(e.score) AS best
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.id
GROUP BY s.name
ORDER BY s.name;
```

## Expected output

```text
Kiran | 81
Leo | 90
Meena | 92
Omar | NULL
Sara | 55
```

## Explanation

- Using `LEFT JOIN` keeps students with no scores, so Omar appears with NULL.
