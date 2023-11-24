-- put the right join at the end to include all salespersons
select sp.salesperson_id,sp.name, coalesce(sum(price),0) total
from 
  sales s
join 
  customer c
  on s.customer_id=c.customer_id
right join 
  salesperson sp
  on sp.salesperson_id=c.salesperson_id
group by 1