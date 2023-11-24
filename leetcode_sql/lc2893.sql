select cast(floor((minute-1)/6)+1 as signed) interval_no
  , sum(order_count) total_orders
from orders
group by 1
order by 1