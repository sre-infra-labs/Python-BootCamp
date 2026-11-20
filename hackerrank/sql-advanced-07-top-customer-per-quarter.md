# Top Customer per Quarter of 2021

- **Language:** SQL
- **Level:** Advanced
- **Topic:** ROW_NUMBER
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each quarter of 2021, find the customer with the highest revenue. Show the quarter, customer and revenue.

## Dataset

Create and load these tables first:

```sql
CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer TEXT, order_date TEXT, amount REAL);
INSERT INTO orders VALUES
(1,'Acme','2020-11-03',1200.0),
(2,'Globex','2021-01-15',800.0),
(3,'Acme','2021-02-20',450.5),
(4,'Initech','2021-04-02',2000.0),
(5,'Globex','2021-05-18',300.0),
(6,'Umbrella','2021-08-09',1500.0),
(7,'Acme','2021-10-12',700.0),
(8,'Initech','2021-11-30',950.0),
(9,'Umbrella','2022-01-05',600.0);
```

## Output format

One line per quarter: `quarter | customer | revenue`.

## Solution

```sql
WITH q AS (
    SELECT customer, (CAST(substr(order_date, 6, 2) AS INTEGER) + 2) / 3 AS qtr, amount
    FROM orders
    WHERE substr(order_date, 1, 4) = '2021'
),
totals AS (
    SELECT qtr, customer, SUM(amount) AS revenue
    FROM q
    GROUP BY qtr, customer
),
ranked AS (
    SELECT qtr, customer, revenue,
           ROW_NUMBER() OVER (PARTITION BY qtr ORDER BY revenue DESC) AS rn
    FROM totals
)
SELECT 'Q' || qtr AS quarter, customer, revenue
FROM ranked
WHERE rn = 1
ORDER BY qtr;
```

## Expected output

```text
Q1 | Globex | 800.0
Q2 | Initech | 2000.0
Q3 | Umbrella | 1500.0
Q4 | Initech | 950.0
```

## Explanation

- Aggregate first, then rank the totals within each quarter.
- `ROW_NUMBER` with `rn = 1` keeps one winner per quarter. Use `RANK` if ties should all be shown.
