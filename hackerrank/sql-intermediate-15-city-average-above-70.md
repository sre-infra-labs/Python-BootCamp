# Cities with High Average Scores

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** HAVING with AVG
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each city, show the average score of its students, rounded to one decimal. Keep only cities whose average is above 70. Sort by city.

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

One line per city: `city | avg_score`.

## Solution

```sql
SELECT s.city, ROUND(AVG(e.score), 1) AS avg_score
FROM students s
JOIN enrollments e ON e.student_id = s.id
GROUP BY s.city
HAVING AVG(e.score) > 70
ORDER BY s.city;
```

## Expected output

```text
Mumbai | 78.0
Pune | 84.3
```

## Explanation

- `HAVING` tests the average of each city group, not individual scores.
