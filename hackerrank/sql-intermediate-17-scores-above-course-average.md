# Scores Above Their Course Average

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Correlated subquery
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List the students whose score is above the average for that course. Show the student name and course title. Sort by name, then title.

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

One line per row: `name | title`.

## Solution

```sql
SELECT s.name, c.title
FROM enrollments e
JOIN students s ON s.id = e.student_id
JOIN courses c ON c.code = e.course_code
WHERE e.score > (SELECT AVG(x.score) FROM enrollments x WHERE x.course_code = e.course_code)
ORDER BY s.name, c.title;
```

## Expected output

```text
Leo | Intro to Programming
Meena | Databases
Meena | Intro to Programming
```

## Explanation

- The subquery is re-run for each enrollment, using that row's course.
