# Login Islands with Start and End

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Gaps and islands
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List every run of consecutive login days per user, with its first day, last day and length. Sort by user, then start day.

## Dataset

Create and load these tables first:

```sql
CREATE TABLE logins (user_name TEXT, login_day TEXT);
INSERT INTO logins VALUES
('ann','2024-01-01'),('ann','2024-01-02'),('ann','2024-01-03'),('ann','2024-01-06'),('ann','2024-01-07'),
('ben','2024-01-02'),('ben','2024-01-03'),('ben','2024-01-09'),
('cy','2024-01-01'),('cy','2024-01-02'),('cy','2024-01-03'),('cy','2024-01-04'),('cy','2024-01-05');
CREATE TABLE invoices (inv_no INTEGER PRIMARY KEY);
INSERT INTO invoices VALUES (1),(2),(3),(5),(6),(9),(10),(11),(12);
CREATE TABLE seats (seat INTEGER PRIMARY KEY, booked INTEGER);
INSERT INTO seats VALUES (1,1),(2,1),(3,0),(4,0),(5,1),(6,1),(7,1),(8,0),(9,0),(10,1);
```

## Output format

One line per run: `user | start | end | days`.

## Solution

```sql
WITH ranked AS (
    SELECT DISTINCT user_name, login_day,
           julianday(login_day) - ROW_NUMBER() OVER (PARTITION BY user_name ORDER BY login_day) AS grp
    FROM logins
),
islands AS (
    SELECT user_name, grp, COUNT(*) AS streak, MIN(login_day) AS start_day, MAX(login_day) AS end_day
    FROM ranked
    GROUP BY user_name, grp
)
SELECT user_name, start_day, end_day, streak AS days
FROM islands
ORDER BY user_name, start_day;
```

## Expected output

```text
ann | 2024-01-01 | 2024-01-03 | 3
ann | 2024-01-06 | 2024-01-07 | 2
ben | 2024-01-02 | 2024-01-03 | 2
ben | 2024-01-09 | 2024-01-09 | 1
cy | 2024-01-01 | 2024-01-05 | 5
```

## Explanation

- `MIN` and `MAX` of the day give the island's boundaries.
