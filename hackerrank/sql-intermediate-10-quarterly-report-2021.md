# Quarterly Report for 2021

- **Language:** SQL
- **Level:** Intermediate
- **Topic:** Date parts and GROUP BY
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original.

## Problem

Using the `orders` table, report the number of orders and total revenue for each quarter of 2021. Quarters with no orders are not shown in this version. Sort by quarter.

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
SELECT 'Q' || ((CAST(substr(order_date, 6, 2) AS INTEGER) + 2) / 3) AS quarter,
       COUNT(*) AS orders,
       ROUND(SUM(amount), 2) AS revenue
FROM orders
WHERE substr(order_date, 1, 4) = '2021'
GROUP BY quarter
ORDER BY quarter;
```

## Expected output

```text
Q1 | 2 | 1250.5
Q2 | 2 | 2300.0
Q3 | 1 | 1500.0
Q4 | 2 | 1650.0
```

## Explanation

- `(month + 2) / 3` maps months 1-3 to 1, 4-6 to 2, and so on, using integer division.
- See the advanced version for a report that shows every quarter, including empty ones.
