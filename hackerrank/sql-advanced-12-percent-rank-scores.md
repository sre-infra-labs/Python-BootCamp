# Percent Rank of Each Score

- **Language:** SQL
- **Level:** Advanced
- **Topic:** PERCENT_RANK
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Compute the percent rank of every enrollment score across all enrollments, rounded to two decimals. Sort by score.

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

One line per row: `name | percent_rank`.

## Solution

```sql
SELECT s.name, ROUND(PERCENT_RANK() OVER (ORDER BY e.score), 2) AS pr
FROM enrollments e
JOIN students s ON s.id = e.student_id
ORDER BY e.score;
```

## Expected output

```text
Sara | 0.0
Leo | 0.17
Kiran | 0.33
Kiran | 0.5
Meena | 0.67
Leo | 0.83
Meena | 1.0
```

## Explanation

- `PERCENT_RANK` is `(rank - 1) / (rows - 1)`, so the lowest score is 0 and the highest is 1.
