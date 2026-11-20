# Scores by Course as Columns

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Pivot with CASE
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Show one row per student with their score in each course: CS101, DB201 and ML301. Use NULL where the student has no score. Sort by name.

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

One line per student: `name | cs101 | db201 | ml301`.

## Solution

```sql
SELECT s.name,
       MAX(CASE WHEN e.course_code = 'CS101' THEN e.score END) AS cs101,
       MAX(CASE WHEN e.course_code = 'DB201' THEN e.score END) AS db201,
       MAX(CASE WHEN e.course_code = 'ML301' THEN e.score END) AS ml301
FROM students s
LEFT JOIN enrollments e ON e.student_id = s.id
GROUP BY s.name
ORDER BY s.name;
```

## Expected output

```text
Kiran | 75 | NULL | 81
Leo | 90 | 67 | NULL
Meena | 88 | 92 | NULL
Omar | NULL | NULL | NULL
Sara | 55 | NULL | NULL
```

## Explanation

- Each `CASE` picks one course's score, and `MAX` collapses the student's rows into one.
