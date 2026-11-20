# Large Orders per Quarter, Including Empty Quarters

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Recursive CTE and LEFT JOIN
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For 2021, count the orders over 1000 and sum their revenue for every quarter Q1 to Q4. Show zero for quarters without such orders.

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

One line per quarter: `quarter | orders | revenue`.

## Solution

```sql
WITH RECURSIVE quarters(q) AS (
    SELECT 1
    UNION ALL
    SELECT q + 1 FROM quarters WHERE q < 4
),
big AS (
    SELECT (CAST(substr(order_date, 6, 2) AS INTEGER) + 2) / 3 AS q, amount
    FROM orders
    WHERE substr(order_date, 1, 4) = '2021' AND amount > 1000
)
SELECT 'Q' || quarters.q AS quarter,
       COUNT(big.amount) AS orders,
       ROUND(COALESCE(SUM(big.amount), 0), 2) AS revenue
FROM quarters
LEFT JOIN big ON big.q = quarters.q
GROUP BY quarters.q
ORDER BY quarters.q;
```

## Expected output

```text
Q1 | 0 | 0.0
Q2 | 1 | 2000.0
Q3 | 1 | 1500.0
Q4 | 0 | 0.0
```

## Explanation

- The recursive CTE creates the four quarters, so a quarter with no matching orders still appears.
- `COUNT(big.amount)` counts only real matches, so empty quarters show 0. Plain `COUNT(*)` would show 1.
