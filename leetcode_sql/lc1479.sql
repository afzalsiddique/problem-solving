SELECT  i.item_category category
       ,SUM(case WHEN dayname(order_date) = 'Monday' THEN quantity else 0 end) 'Monday'
       ,SUM(case WHEN dayname(order_date) = 'Tuesday' THEN quantity else 0 end) 'Tuesday'
       ,SUM(case WHEN dayname(order_date) = 'Wednesday' THEN quantity else 0 end) 'Wednesday'
       ,SUM(case WHEN dayname(order_date) = 'Thursday' THEN quantity else 0 end) 'Thursday'
       ,SUM(case WHEN dayname(order_date) = 'Friday' THEN quantity else 0 end) 'Friday'
       ,SUM(case WHEN dayname(order_date) = 'Saturday' THEN quantity else 0 end) 'Saturday'
       ,SUM(case WHEN dayname(order_date) = 'Sunday' THEN quantity else 0 end) 'Sunday'
FROM orders o
RIGHT JOIN items i
ON o.item_id = i.item_id
GROUP BY  1
order by 1