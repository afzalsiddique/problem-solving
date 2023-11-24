with recursive seq as (
  select 1 ids union select ids+1 from seq where ids<=100
)
select ids
from seq
where ids < (select max(customer_id) from customers)
  and ids <= 100
  and ids not in (select customer_id from customers)
order by 1