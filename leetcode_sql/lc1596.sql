-- cte 
with my_rank as (
    select customer_id, product_id, count(*) freq,
        rank() over(partition by customer_id order by count(*) desc) rk
    from orders
    group by 1,2
)
select r.customer_id,r.product_id,p.product_name from my_rank r
    join products p on p.product_id=r.product_id and r.rk=1

-- 

select r.customer_id,r.product_id,p.product_name
    from (
    select customer_id, product_id, count(*) freq,
        rank() over(partition by customer_id order by count(*) desc) rk
    from orders
    group by 1,2
    ) r
    join products p
    on p.product_id=r.product_id and r.rk=1

