# Courses Nobody Has Taken

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Anti-join
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List the titles of courses with no enrollments.

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

One title per line.

## Solution

```sql
SELECT c.title
FROM courses c
LEFT JOIN enrollments e ON e.course_code = c.code
WHERE e.course_code IS NULL;
```

## Expected output

```text
Artificial Intelligence
```

## Explanation

- Anti-join: `LEFT JOIN` plus `IS NULL` returns the unmatched rows.
