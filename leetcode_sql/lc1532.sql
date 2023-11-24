with cust_rank as (
    select orders.*,
        rank() over(partition by customer_id order by order_date desc) cust_rank
    from orders
)
select c.name customer_name,c.customer_id, o.order_id,o.order_date from customers c
    join orders o using(customer_id)
    join cust_rank using(order_id)
    where cust_rank.cust_rank<=3
    order by 1,2,4 desc