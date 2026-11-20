# Customer Revenue with Cumulative Share

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Window running total
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Total each customer's order amounts across all dates. Sort customers by revenue, highest first. For each, show the revenue and the cumulative share of all revenue, as a percentage with one decimal.

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

One line per customer: `customer | revenue | cumulative_pct`.

## Solution

```sql
WITH totals AS (
    SELECT customer, SUM(amount) AS revenue FROM orders GROUP BY customer
),
grand AS (
    SELECT SUM(revenue) AS total FROM totals
)
SELECT t.customer,
       ROUND(t.revenue, 1) AS revenue,
       ROUND(100.0 * SUM(t.revenue) OVER (ORDER BY t.revenue DESC) / g.total, 1) AS cumulative_pct
FROM totals t
CROSS JOIN grand g
ORDER BY t.revenue DESC;
```

## Expected output

```text
Initech | 2950.0 | 34.7
Acme | 2350.5 | 62.4
Umbrella | 2100.0 | 87.1
Globex | 1100.0 | 100.0
```

## Explanation

- A running sum over revenue sorted descending gives the cumulative amount.
- Dividing by the grand total turns it into a share.
