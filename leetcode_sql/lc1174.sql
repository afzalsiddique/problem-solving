WITH t1 AS -- first order of each customer
(
	SELECT  customer_id
	       ,MIN(order_date) first_order
	FROM delivery
	GROUP BY  1
)
, t2 as ( -- immediate order
  SELECT  t1.customer_id
        ,t1.first_order
        ,customer_pref_delivery_date
  FROM t1
  JOIN delivery d
  ON t1.customer_id = d.customer_id
    and t1.first_order=d.order_date
    and t1.first_order=d.customer_pref_delivery_date
)
SELECT
  round(
    (SELECT COUNT(*) FROM t2) / (SELECT COUNT(*) FROM t1)*100 
    ,2
  )
  AS immediate_percentage;