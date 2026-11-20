# Average Score per Course

- **Language:** SQL
- **Level:** Beginner
- **Topic:** AVG and ROUND
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each course code, show the average score rounded to one decimal place. Sort by course code.

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

One line per course: `code | avg_score`.

## Solution

```sql
SELECT course_code, ROUND(AVG(score), 1) AS avg_score FROM enrollments GROUP BY course_code ORDER BY course_code;
```

## Expected output

```text
CS101 | 77.0
DB201 | 79.5
ML301 | 81.0
```

## Explanation

- `AVG` gives a decimal here because `score` is an integer and SQLite divides as a float.
