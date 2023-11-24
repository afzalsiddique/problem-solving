with min_year as (
  select product_id, min(year) first_year
  from sales
  group by 1
)
select product_id, year first_year, quantity, price
from sales
where (product_id, year) in (select * from min_year)