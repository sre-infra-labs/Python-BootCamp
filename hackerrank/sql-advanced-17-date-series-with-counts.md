# Orders per Day with Empty Days

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Generated date series
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

For each day from 2021-01-14 to 2021-01-16, count the orders. Show days with no orders as 0.

## Dataset

Create and load these tables first:

```sql
CREATE TABLE orders (order_id INTEGER PRIMARY KEY, customer TEXT, order_date TEXT, amount REAL);
INSERT INTO orders VALUES
(1,'Acme','2020-11-03',1200.0),(2,'Globex','2021-01-15',800.0),(3,'Acme','2021-02-20',450.5),
(4,'Initech','2021-04-02',2000.0),(5,'Globex','2021-05-18',300.0),(6,'Umbrella','2021-08-09',1500.0),
(7,'Acme','2021-10-12',700.0),(8,'Initech','2021-11-30',950.0),(9,'Umbrella','2022-01-05',600.0);
```

## Output format

One line per day: `date | orders`.

## Solution

```sql
WITH RECURSIVE days(d) AS (
    SELECT '2021-01-14'
    UNION ALL
    SELECT date(d, '+1 day') FROM days WHERE d < '2021-01-16'
)
SELECT days.d, COUNT(o.order_id) AS orders
FROM days
LEFT JOIN orders o ON o.order_date = days.d
GROUP BY days.d
ORDER BY days.d;
```

## Expected output

```text
2021-01-14 | 0
2021-01-15 | 1
2021-01-16 | 0
```

## Explanation

- The recursive CTE generates the dates, and the `LEFT JOIN` keeps days with no orders.
