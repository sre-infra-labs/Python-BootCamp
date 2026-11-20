# Missing Invoice Number Ranges

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Gaps with LAG
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Find the ranges of invoice numbers that are missing between the first and last invoice. Show each range's start and end, sorted by start.

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

One line per range: `gap_start | gap_end`.

## Solution

```sql
SELECT t.prev_no + 1 AS gap_start, t.inv_no - 1 AS gap_end
FROM (
    SELECT inv_no, LAG(inv_no) OVER (ORDER BY inv_no) AS prev_no
    FROM invoices
) t
WHERE t.prev_no IS NOT NULL AND t.inv_no - t.prev_no > 1
ORDER BY gap_start;
```

## Expected output

```text
4 | 4
7 | 8
```

## Explanation

- `LAG` gives the previous number. If the difference is more than 1, the numbers in between are missing.
