# Split Scores into Two Halves

- **Language:** SQL
- **Level:** Advanced
- **Topic:** NTILE
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Split all enrollment scores into two groups of nearly equal size using `NTILE(2)`, lowest scores first. Show the name, score and group number. Sort by score.

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

One line per row: `name | score | group`.

## Solution

```sql
SELECT s.name, e.score, NTILE(2) OVER (ORDER BY e.score) AS grp
FROM enrollments e
JOIN students s ON s.id = e.student_id
ORDER BY e.score;
```

## Expected output

```text
Sara | 55 | 1
Leo | 67 | 1
Kiran | 75 | 1
Kiran | 81 | 1
Meena | 88 | 2
Leo | 90 | 2
Meena | 92 | 2
```

## Explanation

- When rows do not divide evenly, `NTILE` gives the extra row to the first groups.
