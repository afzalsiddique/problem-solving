with t as (
  select product_id
    , year(purchase_date) year
    , count(*) times
  from orders
  group by 1,2
)
-- select * from t
select distinct t1.product_id
from t t1
join t t2
  on t1.product_id=t2.product_id
  and t1.year!=t2.year
  and t1.year=t2.year+1
where t1.times>=3
  and t2.times>=3
