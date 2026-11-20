# Top Student per Course with FIRST_VALUE

- **Language:** SQL
- **Level:** Advanced
- **Topic:** FIRST_VALUE
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each course, show the name of the student with the highest score. Sort by course title.

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

One line per course: `title | top_student`.

## Solution

```sql
SELECT DISTINCT c.title,
       FIRST_VALUE(s.name) OVER (PARTITION BY e.course_code ORDER BY e.score DESC) AS top_student
FROM enrollments e
JOIN students s ON s.id = e.student_id
JOIN courses c ON c.code = e.course_code
ORDER BY c.title;
```

## Expected output

```text
Databases | Meena
Intro to Programming | Leo
Machine Learning | Kiran
```

## Explanation

- `FIRST_VALUE` repeats the winner on each row of its partition, so `DISTINCT` leaves one row per course.
