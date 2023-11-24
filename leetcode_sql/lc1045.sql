with total_product as (
    select count(*) no_of_total_products from product
)
select customer_id
from customer c
group by 1
having count(distinct product_key)=(select count(*) no_of_total_products from product)