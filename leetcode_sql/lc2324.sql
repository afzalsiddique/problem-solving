with t1 as ( -- toal spending on each product by each user
  select user_id
    , s.product_id
    , sum(quantity*price) spending
  from sales s
  join product p
  on p.product_id=s.product_id
  group by 1,2
)
-- select * from t1
, t2 as ( -- max spending for each user
  select user_id
    , max(spending) spending
  from t1
  group by 1
)
select t1.user_id
  , t1.product_id
from t1
join t2
on t1.user_id=t2.user_id
 and t1.spending=t2.spending