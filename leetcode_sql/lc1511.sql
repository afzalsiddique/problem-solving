-- can be visualized
SELECT customer_id, name
FROM (
    SELECT c.customer_id, c.name, 
    SUM(CASE WHEN LEFT(o.order_date, 7) = '2020-06' THEN p.price*o.quantity ELSE 0 END) AS t1, 
    SUM(CASE WHEN LEFT(o.order_date, 7) = '2020-07' THEN p.price*o.quantity ELSE 0 END) AS t2
    FROM customers c
    JOIN orders o
    ON c.customer_id = o.customer_id
    JOIN product p
    ON p.product_id = o.product_id
    GROUP BY 1
    ) tmp
WHERE t1 >= 100 AND t2 >= 100

-- 
select c.customer_id, name from customers c
    inner join orders o on o.customer_id=c.customer_id
    inner join product p on o.product_id=p.product_id
group by 1
having sum(if(left(order_date,7)='2020-06',quantity,0)*price)>=100
    and sum(if(left(order_date,7)='2020-07',quantity,0)*price)>=100