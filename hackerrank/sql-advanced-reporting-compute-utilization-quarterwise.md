# Compute Utilization Report: Quarter-wise for 2021

- **Language:** SQL
- **Level:** Advanced
- **Topic:** Date overlap, aggregation and formatted output by quarter
- **Practice more:** https://www.hackerrank.com/domains/sql

> Written for this repo in the style of HackerRank practice problems. The wording and the solution are original. The instance types, sizing names and deployment times are sample values, not from a real account.

## Problem

A cloud team runs EC2 instances in deployments. A deployment starts at `dt_start` and ends at `dt_end`. If `dt_end` is NULL, the instance is still running.

Write a SQL query that reports the compute cost of each configuration for each quarter of 2021. For each quarter, count only the hours that fall inside both the deployment and the quarter. Show each quarter as `$cost = hours hours * $price/hr`, where the cost is the hours times the configuration's `price_per_hour`. Show the configuration's `name`. Show every configuration, even one with no 2021 usage, with zero values for quarters without usage.

Deployments can start before 2021, end in 2022, or cross a quarter boundary. Use exact timestamps, not whole days.

## Input tables

- `configurations(id, name, price_per_hour)`: `id` is the instance type, `name` is the sizing label
- `deployments(configuration_id, dt_start, dt_end)`: `dt_end` is NULL while the instance is running

## Output format

One line per configuration, sorted by `name`: `configuration | Q1'21 | Q2'21 | Q3'21 | Q4'21`. Each quarter cell looks like `$cost = hours hours * $price/hr`, with the cost and hours to 2 decimals and the price to 4 decimals.

Example: `$121.00 = 350.00 hours * $0.0310/hr`

## Dataset

Create and load these tables first:

```sql
CREATE TABLE configurations (id TEXT PRIMARY KEY, name TEXT, price_per_hour REAL);
INSERT INTO configurations VALUES
('c4.xlarge',  '4vpu.15gbram.250gbssd',   0.1990),
('m5.large',   '2vpu.8gbram.100gbssd',    0.0960),
('r5.2xlarge', '8vpu.64gbram.500gbssd',   0.5040),
('t3.medium',  '2vpu.4gbram.50gbssd',     0.0416);
CREATE TABLE deployments (configuration_id TEXT, dt_start TEXT, dt_end TEXT);
INSERT INTO deployments VALUES
('c4.xlarge', '2020-11-20 09:15:00', '2021-01-06 18:40:00'),
('c4.xlarge', '2021-02-11 08:30:00', '2021-03-19 17:05:00'),
('c4.xlarge', '2021-05-03 22:00:00', '2021-08-14 06:45:00'),
('c4.xlarge', '2021-11-29 12:00:00', NULL),
('m5.large',  '2021-01-15 00:00:00', '2021-07-20 12:00:00'),
('m5.large',  '2021-09-01 06:00:00', '2022-02-10 10:00:00'),
('r5.2xlarge','2021-03-28 16:20:00', '2021-04-02 09:10:00'),
('r5.2xlarge','2021-10-12 11:00:00', '2021-10-12 23:30:00'),
('t3.medium', '2020-06-01 00:00:00', '2020-12-31 23:59:59'),
('t3.medium', '2021-06-30 20:00:00', '2021-07-01 04:00:00');
```

## Solution

```sql
WITH quarters(q, qs, qe) AS (
    VALUES ('Q1''21', '2021-01-01 00:00:00', '2021-04-01 00:00:00'),
           ('Q2''21', '2021-04-01 00:00:00', '2021-07-01 00:00:00'),
           ('Q3''21', '2021-07-01 00:00:00', '2021-10-01 00:00:00'),
           ('Q4''21', '2021-10-01 00:00:00', '2022-01-01 00:00:00')
),
usage AS (
    SELECT d.configuration_id AS cid, q.q,
           SUM(MAX(0, julianday(MIN(COALESCE(d.dt_end, '9999-12-31 23:59:59'), q.qe))
                      - julianday(MAX(d.dt_start, q.qs))) * 24) AS hrs
    FROM deployments d
    CROSS JOIN quarters q
    GROUP BY d.configuration_id, q.q
),
wide AS (
    SELECT c.name, c.price_per_hour AS price,
           COALESCE(SUM(CASE WHEN u.q = 'Q1''21' THEN u.hrs END), 0) AS h1,
           COALESCE(SUM(CASE WHEN u.q = 'Q2''21' THEN u.hrs END), 0) AS h2,
           COALESCE(SUM(CASE WHEN u.q = 'Q3''21' THEN u.hrs END), 0) AS h3,
           COALESCE(SUM(CASE WHEN u.q = 'Q4''21' THEN u.hrs END), 0) AS h4
    FROM configurations c
    LEFT JOIN usage u ON u.cid = c.id
    GROUP BY c.id, c.name, c.price_per_hour
)
SELECT name AS configuration,
       printf('$%.2f = %.2f hours * $%.4f/hr', h1 * price, h1, price) AS "Q1'21",
       printf('$%.2f = %.2f hours * $%.4f/hr', h2 * price, h2, price) AS "Q2'21",
       printf('$%.2f = %.2f hours * $%.4f/hr', h3 * price, h3, price) AS "Q3'21",
       printf('$%.2f = %.2f hours * $%.4f/hr', h4 * price, h4, price) AS "Q4'21"
FROM wide
ORDER BY name;
```

## Expected output

```text
2vpu.4gbram.50gbssd | $0.00 = 0.00 hours * $0.0416/hr | $0.17 = 4.00 hours * $0.0416/hr | $0.17 = 4.00 hours * $0.0416/hr | $0.00 = 0.00 hours * $0.0416/hr
2vpu.8gbram.100gbssd | $175.10 = 1824.00 hours * $0.0960/hr | $209.66 = 2184.00 hours * $0.0960/hr | $113.47 = 1182.00 hours * $0.0960/hr | $211.97 = 2208.00 hours * $0.0960/hr
4vpu.15gbram.250gbssd | $201.24 = 1011.25 hours * $0.1990/hr | $277.41 = 1394.00 hours * $0.1990/hr | $211.49 = 1062.75 hours * $0.1990/hr | $155.22 = 780.00 hours * $0.1990/hr
8vpu.64gbram.500gbssd | $40.15 = 79.67 hours * $0.5040/hr | $16.72 = 33.17 hours * $0.5040/hr | $0.00 = 0.00 hours * $0.5040/hr | $6.30 = 12.50 hours * $0.5040/hr
```

## Explanation

- The `quarters` CTE holds each quarter's start and end. A `CROSS JOIN` pairs every deployment with every quarter.
- The overlap is `MIN(end, quarter_end) - MAX(start, quarter_start)`. `MAX(0, ...)` gives 0 when the two periods don't overlap.
- A NULL `dt_end` means the instance is still running, so `COALESCE` uses a far-future date.
- `julianday` turns timestamps into fractional days, so multiplying by 24 gives exact hours, including partial days.
- The `wide` CTE pivots the quarterly hours into one row per configuration, and `printf` builds the `$cost = hours hours * $price/hr` text.
- `LEFT JOIN` keeps configurations with no 2021 usage. Their quarters show zero.
- The cost is computed from unrounded hours, so the displayed hours times the displayed price can differ from the displayed cost in the last cent.
