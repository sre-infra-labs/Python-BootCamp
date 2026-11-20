# Month-over-Month Revenue Change in 2021

- **Language:** SQL
- **Level:** Advanced
- **Topic:** LAG on aggregates
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Show the revenue for each month of 2021 that has orders, and the change from the previous month that has orders. Sort by month.

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

One line per month: `month | revenue | change`. NULL for the first month.

## Solution

```sql
WITH monthly AS (
    SELECT substr(order_date, 1, 7) AS month, SUM(amount) AS revenue
    FROM orders
    WHERE substr(order_date, 1, 4) = '2021'
    GROUP BY month
)
SELECT month, revenue, revenue - LAG(revenue) OVER (ORDER BY month) AS change
FROM monthly
ORDER BY month;
```

## Expected output

```text
2021-01 | 800.0 | NULL
2021-02 | 450.5 | -349.5
2021-04 | 2000.0 | 1549.5
2021-05 | 300.0 | -1700.0
2021-08 | 1500.0 | 1200.0
2021-10 | 700.0 | -800.0
2021-11 | 950.0 | 250.0
```

## Explanation

- Aggregate to months first, then apply `LAG` to the monthly rows.
- March has no orders, so the change for April compares with February.
