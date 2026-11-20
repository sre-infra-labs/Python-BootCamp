# Rank Students within Each Course

- **Language:** SQL
- **Level:** Advanced
- **Topic:** RANK in partitions
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Rank the students in each course by score, highest first. Equal scores share a rank. Sort by course title, rank, then name.

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

One line per row: `title | name | score | rank`.

## Solution

```sql
SELECT c.title, s.name, e.score,
       RANK() OVER (PARTITION BY e.course_code ORDER BY e.score DESC) AS rnk
FROM enrollments e
JOIN students s ON s.id = e.student_id
JOIN courses c ON c.code = e.course_code
ORDER BY c.title, rnk, s.name;
```

## Expected output

```text
Databases | Meena | 92 | 1
Databases | Leo | 67 | 2
Intro to Programming | Leo | 90 | 1
Intro to Programming | Meena | 88 | 2
Intro to Programming | Kiran | 75 | 3
Intro to Programming | Sara | 55 | 4
Machine Learning | Kiran | 81 | 1
```

## Explanation

- `PARTITION BY course_code` restarts the ranking for each course.
