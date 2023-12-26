---
title: Welcome to Notion-Budget-Tracker
---

<DataTable
  data={transactions}
  rows=6
  search="true"
  />

<BarChart 
  data={transactions_per_day} 
  x=day
  y=transactions 
  fillColor="#488f96"
  ></BarChart>

```sql transactions
SELECT * FROM transactions
```

```sql transactions_per_day
SELECT
  DATE_TRUNC('day', propDate) as day, 
  COUNT(*) as transactions
FROM ${transactions}
GROUP BY 1
ORDER BY 1
```