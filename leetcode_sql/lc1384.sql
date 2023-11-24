with a as (
SELECT  
      product_id
      ,period_start
      ,period_end
      ,average_daily_sales
       ,greatest(DATEDIFF(least('2018-12-31',period_end),greatest('2018-01-01',period_start))+1,0) y_2018
       ,greatest(DATEDIFF(least('2019-12-31',period_end),greatest('2019-01-01',period_start))+1,0) y_2019
       ,greatest(DATEDIFF(least('2020-12-31',period_end),greatest('2020-01-01',period_start))+1,0) y_2020
FROM sales
)
-- select * from a
, b 
(product_id, report_year,total_amount) as  (
  select product_id
    , '2018'
    , sum(average_daily_sales*y_2018)
  from a
  group by product_id
  union
  select product_id
    , '2019'
    , sum(average_daily_sales*y_2019)
  from a
  group by product_id
  union
  select product_id
    , '2020'
    , sum(average_daily_sales*y_2020)
  from a
  group by product_id
)
select p.product_id
  , p.product_name
  , report_year
  , total_amount
from product p
join b
on p.product_id=b.product_id
where total_amount>0
order by 1,3