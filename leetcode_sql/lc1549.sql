with mostrecent as (
    select product_id,max(order_date) from orders
    group by 1
)
select p.product_name,p.product_id,o.order_id,o.order_date
    from products p join orders o using(product_id)
where (p.product_id,o.order_date) in (select * from mostrecent)
order by 1,2,3