with zero as (
  select distinct customer_id
  from orders
  where order_type=0
)
select order_id
  , customer_id
  , order_type
from orders
where customer_id not in (
  select customer_id from zero
)
union
select o.order_id
  , o.customer_id
  , o.order_type
from orders o
join zero
on o.customer_id=zero.customer_id
where order_type=0