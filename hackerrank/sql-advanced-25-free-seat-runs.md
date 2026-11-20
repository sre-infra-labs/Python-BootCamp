# Runs of Free Seats

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Gaps and islands on seats
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Find each run of consecutive free seats (where `booked = 0`). Show the first seat, last seat, and number of seats in the run. Sort by first seat.

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

One line per run: `first | last | seats`.

## Solution

```sql
WITH free AS (
    SELECT seat, seat - ROW_NUMBER() OVER (ORDER BY seat) AS grp
    FROM seats
    WHERE booked = 0
)
SELECT MIN(seat) AS first_seat, MAX(seat) AS last_seat, COUNT(*) AS free_seats
FROM free
GROUP BY grp
ORDER BY first_seat;
```

## Expected output

```text
3 | 4 | 2
8 | 9 | 2
```

## Explanation

- The same island trick works on any integer column, not only dates.
