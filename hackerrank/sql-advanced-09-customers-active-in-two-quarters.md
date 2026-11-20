# Customers Active in at Least Two Quarters of 2021

- **Language:** SQL
- **Level:** Advanced
- **Topic:** HAVING with DISTINCT
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

List the customers who placed orders in at least two different quarters of 2021. Sort by name.

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

One name per line.

## Solution

```sql
WITH q AS (
    SELECT DISTINCT customer, (CAST(substr(order_date, 6, 2) AS INTEGER) + 2) / 3 AS qtr
    FROM orders
    WHERE substr(order_date, 1, 4) = '2021'
)
SELECT customer
FROM q
GROUP BY customer
HAVING COUNT(*) >= 2
ORDER BY customer;
```

## Expected output

```text
Acme
Globex
Initech
```

## Explanation

- `DISTINCT` on (customer, quarter) counts each quarter once per customer, even with several orders in it.
