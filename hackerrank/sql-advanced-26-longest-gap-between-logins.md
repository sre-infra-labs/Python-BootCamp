# Longest Gap Between Logins

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Gaps with LAG on dates
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each user, find the longest number of days between two consecutive logins. Sort by user.

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

One line per user: `user | longest_gap_days`.

## Solution

```sql
WITH g AS (
    SELECT user_name,
           julianday(login_day) - julianday(LAG(login_day) OVER (PARTITION BY user_name ORDER BY login_day)) AS gap
    FROM logins
)
SELECT user_name, CAST(MAX(gap) AS INTEGER) AS longest_gap_days
FROM g
GROUP BY user_name
ORDER BY user_name;
```

## Expected output

```text
ann | 3
ben | 6
cy | 1
```

## Explanation

- `julianday` turns dates into numbers, so subtraction gives days.
- The first login of each user has no previous row, so its gap is NULL and `MAX` ignores it.
