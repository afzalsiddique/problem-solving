with freq as (
    select buyer_id, count(*) buy_freq
    from orders
    where year(order_date)=2019
    group by 1
)
select user_id buyer_id,join_date,
    coalesce(
        buy_freq 
    ,0) orders_in_2019
from users u left join freq f
on u.user_id=f.buyer_id