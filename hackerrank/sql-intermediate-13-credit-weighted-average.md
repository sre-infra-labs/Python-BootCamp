# Credit-Weighted Average Score

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Weighted averages
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each student, compute the average score weighted by course credits. Round to two decimals. Sort by name.

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

One line per student: `name | weighted_avg`.

## Solution

```sql
SELECT s.name,
       ROUND(SUM(e.score * c.credits) * 1.0 / SUM(c.credits), 2) AS weighted_avg
FROM students s
JOIN enrollments e ON e.student_id = s.id
JOIN courses c ON c.code = e.course_code
GROUP BY s.name
ORDER BY s.name;
```

## Expected output

```text
Kiran | 78.0
Leo | 80.14
Meena | 89.71
Sara | 55.0
```

## Explanation

- Multiply each score by its credits, then divide by the total credits.
- `* 1.0` avoids integer division.
