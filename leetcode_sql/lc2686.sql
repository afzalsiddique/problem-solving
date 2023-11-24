SELECT  order_date
       ,round( SUM(order_date = customer_pref_delivery_date) / COUNT(*) * 100 ,2 ) immediate_percentage
FROM delivery
GROUP BY  1
ORDER BY 1