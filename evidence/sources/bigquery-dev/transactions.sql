WITH
  transactions AS (
  SELECT
    * EXCEPT(row_number)
  FROM (
    SELECT
      *,
      ROW_NUMBER() OVER (PARTITION BY id ORDER BY last_edited_time DESC) row_number
    FROM
      `coucou-le-projet.budget.raw_transactions__duplicated`)
  WHERE
    row_number = 1)
SELECT
  id,
  url,
  created_by,
  parent,
  archived,
  properties.Name.title[0].plain_text as propTitle,
  properties.Amount.number as propAmount,
  properties.Category.`select`.name as propCategory,
  properties.`Date`.`date`.start as propDate,
  last_edited_by,
  last_edited_time,
  created_time
FROM
  transactions