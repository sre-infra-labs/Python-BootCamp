# Students per Course Title

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** LEFT JOIN and COUNT
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each course title, count the students enrolled, including courses with no students. Sort by title.

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

One line per course: `title | students`.

## Solution

```sql
SELECT c.title, COUNT(e.student_id) AS students
FROM courses c
LEFT JOIN enrollments e ON e.course_code = c.code
GROUP BY c.title
ORDER BY c.title;
```

## Expected output

```text
Artificial Intelligence | 0
Databases | 2
Intro to Programming | 4
Machine Learning | 1
```

## Explanation

- `COUNT(e.student_id)` counts only real matches, so an empty course shows 0.
