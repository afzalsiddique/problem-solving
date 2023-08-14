with total as
         (select count(*) total
          from product)
select customer_id
from customer
group by customer_id
having count(distinct product_key) = (select total from total)
;
