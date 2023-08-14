with total as
         (select count(*) total
          from product)
select customer_id
from customer
group by customer_id
having count(distinct product_key) = (select total from total)
;
--
with t as (
    select count(distinct product_key) total from product
)
select customer_id, count(distinct product_key) dis
from customer c
where dis=(select total from t)
group by customer_id


